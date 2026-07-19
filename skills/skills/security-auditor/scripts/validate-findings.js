#!/usr/bin/env node
/**
 * Minimal schema-ish validator for findings.json produced by security-auditor.
 * Zero external dependencies. Checks required structure and enums.
 * Usage: node validate-findings.js [path/to/findings.json]
 */

const fs = require('fs');
const path = require('path');

const file = process.argv[2] || 'findings.json';

if (!fs.existsSync(file)) {
  console.error(`File not found: ${file}`);
  process.exit(1);
}

let data;
try {
  data = JSON.parse(fs.readFileSync(file, 'utf8'));
} catch (e) {
  console.error('Invalid JSON:', e.message);
  process.exit(1);
}

const errors = [];

function req(obj, key, ctx) {
  if (obj == null || !(key in obj)) {
    errors.push(`${ctx}: missing required field "${key}"`);
    return false;
  }
  return true;
}

// Top level
if (!req(data, 'audit_metadata', 'root')) process.exit(report());
if (!req(data, 'findings', 'root')) process.exit(report());

const meta = data.audit_metadata;
['project', 'timestamp', 'scope', 'phases_completed'].forEach(k => req(meta, k, 'audit_metadata'));

if (!Array.isArray(data.findings)) {
  errors.push('findings must be an array');
} else {
  const severities = new Set(['Critical', 'High', 'Medium', 'Low']);
  const categories = new Set(['security', 'logic', 'ambiguity', 'bug']);
  const confidences = new Set(['high', 'medium', 'low']);
  const statuses = new Set(['confirmed', 'rejected', 'needs-more-info']);

  data.findings.forEach((f, i) => {
    const ctx = `findings[${i}]`;
    ['id', 'title', 'severity', 'category', 'location', 'scenario', 'impact', 'confidence', 'status']
      .forEach(k => req(f, k, ctx));

    if (f.severity && !severities.has(f.severity)) {
      errors.push(`${ctx}.severity must be one of ${[...severities].join(', ')}`);
    }
    if (f.category && !categories.has(f.category)) {
      errors.push(`${ctx}.category must be one of ${[...categories].join(', ')}`);
    }
    if (f.confidence && !confidences.has(f.confidence)) {
      errors.push(`${ctx}.confidence must be one of ${[...confidences].join(', ')}`);
    }
    if (f.status && !statuses.has(f.status)) {
      errors.push(`${ctx}.status must be one of ${[...statuses].join(', ')}`);
    }
    if (f.location && !req(f.location, 'paths', `${ctx}.location`)) {
      // already recorded
    } else if (f.location && !Array.isArray(f.location.paths)) {
      errors.push(`${ctx}.location.paths must be an array`);
    }
  });
}

function report() {
  if (errors.length === 0) {
    console.log(`OK — ${file} is structurally valid (${data.findings.length} findings)`);
    return 0;
  }
  console.error(`Validation failed for ${file}:`);
  errors.forEach(e => console.error('  - ' + e));
  return 1;
}

process.exit(report());
