#!/usr/bin/env node
'use strict';
// Dependency-free structural validator for the adjacent findings schema, not a
// general JSON Schema engine. "format" is annotation-only (Draft 2020-12 default).
// No report content, unknown property names or parser excerpts enter diagnostics.
const fs = require('fs');
const path = require('path');
const schema = JSON.parse(fs.readFileSync(
  path.join(__dirname, '../references/findings-schema.json'), 'utf8'));
const owns = (object, key) => Object.prototype.hasOwnProperty.call(object, key);
const isObject = value => value !== null && typeof value === 'object' && !Array.isArray(value);
const supported = new Set(['$schema', '$id', 'title', 'description', 'type', 'required',
  'properties', 'items', 'enum', 'format', 'additionalProperties', 'minLength',
  'minItems', 'minimum']);

function checkSchema(rule) {
  for (const key of Object.keys(rule)) {
    if (!supported.has(key)) throw new Error('Unsupported schema keyword');
  }
  if (!['object', 'array', 'string', 'boolean', 'integer'].includes(rule.type)) {
    throw new Error('Unsupported schema type');
  }
  for (const child of Object.values(rule.properties || {})) checkSchema(child);
  if (rule.items) checkSchema(rule.items);
  if (isObject(rule.additionalProperties)) checkSchema(rule.additionalProperties);
}

function validateDocument(data) {
  checkSchema(schema);
  const errors = [];
  const fail = message => { if (errors.length < 30) errors.push(message); };
  function visit(value, rule, context) {
    const validType = rule.type === 'object' ? isObject(value)
      : rule.type === 'array' ? Array.isArray(value)
      : rule.type === 'integer' ? Number.isSafeInteger(value)
      : typeof value === rule.type;
    if (!validType) { fail(context + ': invalid type'); return; }
    if (rule.enum && !rule.enum.includes(value)) fail(context + ': invalid enum');
    if (rule.type === 'string' && Array.from(value).length < (rule.minLength || 0)) {
      fail(context + ': string too short');
    }
    if (rule.minimum !== undefined && value < rule.minimum) fail(context + ': below minimum');
    if (rule.type === 'array') {
      if (value.length < (rule.minItems || 0)) fail(context + ': too few items');
      value.forEach((item, index) => visit(item, rule.items, context + '[' + index + ']'));
    }
    if (rule.type === 'object') {
      for (const key of rule.required || []) {
        if (!owns(value, key)) fail(context + '.' + key + ': required');
      }
      for (const [key, child] of Object.entries(rule.properties || {})) {
        if (owns(value, key)) visit(value[key], child, context + '.' + key);
      }
      for (const key of Object.keys(value)) {
        if (owns(rule.properties || {}, key)) continue;
        if (rule.additionalProperties === false) fail(context + ': unexpected property');
        else if (isObject(rule.additionalProperties)) {
          visit(value[key], rule.additionalProperties, context + '.<additional>');
        }
      }
    }
  }
  visit(data, schema, 'root');
  if (errors.length) return errors;
  const ids = new Set();
  const confirmed = data.findings.filter(finding => finding.status === 'confirmed');
  data.findings.forEach((finding, index) => {
    if (ids.has(finding.id)) fail('findings[' + index + '].id: duplicate');
    ids.add(finding.id);
  });
  if (data.summary) {
    if (owns(data.summary, 'total_confirmed') && data.summary.total_confirmed !== confirmed.length) {
      fail('summary.total_confirmed: inconsistent');
    }
    for (const [field, property] of [['by_severity', 'severity'], ['by_category', 'category']]) {
      const counts = data.summary[field];
      if (!counts) continue;
      for (const [key, value] of Object.entries(counts)) {
        if (value !== confirmed.filter(finding => finding[property] === key).length) {
          fail('summary.' + field + ': inconsistent count');
        }
      }
    }
  }
  return errors;
}

function main(args) {
  if (args.length === 1 && args[0] === '--help') {
    console.log('Usage: node validate-findings.js /explicit/path/to/findings.json');
    console.log('Exit 0: structure valid; 1: invalid report; 2: usage/input/schema unavailable.');
    return 0;
  }
  if (args.length !== 1 || args[0].startsWith('--')) {
    console.error('Expected one explicit report path; use --help.');
    return 2;
  }
  let fd;
  let bytes;
  try {
    if (!Number.isInteger(fs.constants.O_NOFOLLOW) || !Number.isInteger(fs.constants.O_NONBLOCK)) {
      throw new Error('Safe input flags unavailable');
    }
    fd = fs.openSync(args[0], fs.constants.O_RDONLY | fs.constants.O_NOFOLLOW | fs.constants.O_NONBLOCK);
    const stat = fs.fstatSync(fd);
    const maxBytes = 5 * 1024 * 1024;
    if (!stat.isFile() || stat.size > maxBytes) throw new Error('Unsupported input');
    // Bounded read also handles a regular file growing after the size check.
    const buffer = Buffer.alloc(maxBytes + 1);
    let length = 0;
    while (length < buffer.length) {
      const count = fs.readSync(fd, buffer, length, buffer.length - length, null);
      if (!count) break;
      length += count;
    }
    if (length > maxBytes) throw new Error('Input too large');
    bytes = buffer.subarray(0, length).toString('utf8');
  } catch {
    console.error('Input unavailable: require safe file flags and a readable regular file, not a symlink, at most 5 MiB.');
    return 2;
  } finally {
    if (fd !== undefined) fs.closeSync(fd);
  }
  let data;
  try { data = JSON.parse(bytes); }
  catch { console.error('Invalid JSON (contents withheld).'); return 1; }
  let errors;
  try { errors = validateDocument(data); }
  catch { console.error('Validator/schema mismatch; validation unavailable.'); return 2; }
  if (errors.length) {
    console.error('Invalid report (up to 30 structural/consistency errors):');
    errors.forEach(error => console.error('  - ' + error));
    return 1;
  }
  console.log('OK: report structure and checked counts are valid; factual claims and date-time format are not verified.');
  return 0;
}

module.exports = { validateDocument };
if (require.main === module) process.exitCode = main(process.argv.slice(2));
