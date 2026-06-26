You are given an Apache-style access log located at:

/app/access.log

Your task is to generate a JSON report at:

/app/report.json

---

## Output Requirements

The output file must be valid JSON and contain exactly the following fields:

- total_requests (integer)
- unique_ips (integer)
- top_path (string)

No additional fields are allowed.

---

## Definitions

1. total_requests  
   The number of non-empty lines in `/app/access.log`.

2. unique_ips  
   The number of unique IP addresses.  
   The IP address is the first whitespace-separated token on each line.

3. top_path  
   The most frequently requested URL path extracted from HTTP request lines.  
   The path is captured from lines matching HTTP methods (GET, POST, PUT, DELETE, HEAD, PATCH).

---

## Success Criteria

A solution is correct only if all of the following are true:

1. `/app/report.json` exists
2. `/app/report.json` is valid JSON and contains exactly the keys:
   - total_requests
   - unique_ips
   - top_path
3. The values in `/app/report.json` exactly match the computed values from `/app/access.log` according to the definitions above