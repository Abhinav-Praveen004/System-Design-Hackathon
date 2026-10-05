import base64
import urllib.request
import re
import os
import json
import zlib

files = [
    "02_HLD\\system_context_diagram.md",
    "02_HLD\\hld_architecture.md",
    "02_HLD\\container_diagram.md"
]

req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for f in files:
    if os.path.exists(f):
        with open(f, 'r') as file:
            content = file.read()
        match = re.search(r'```mermaid\s*(.*?)\s*```', content, re.DOTALL)
        if match:
            mermaid_code = match.group(1).strip()
            
            # encode using pako style which mermaid.ink uses
            state = json.dumps({"code": mermaid_code, "mermaid": "{\"theme\": \"default\"}"}).encode('utf-8')
            compressor = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS)
            compressed = compressor.compress(state) + compressor.flush()
            encoded2 = base64.urlsafe_b64encode(compressed).decode('utf-8').rstrip('=')
            
            url = f"https://mermaid.ink/img/pako:{encoded2}"
            out_file = f.replace('.md', '.png')
            try:
                req = urllib.request.Request(url, headers=req_headers)
                with urllib.request.urlopen(req) as response, open(out_file, 'wb') as out_f:
                    out_f.write(response.read())
                print(f"Success for {f}")
            except Exception as e:
                print(f"Failed {f} with pako: {e}")
                
