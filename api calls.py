import requests

from requests.structures import CaseInsensitiveDict

url = "https://api.pepperi.com/v1.0/items"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjIwZDZkZDMzMzkzYmZkMWNkYTc2YjRmNjQ5NGRmNzYzIiwidHlwIjoiSldUIn0.eyJuYmYiOjE2NDgyMTA0MjQsImV4cCI6MTY0ODIxNDAyNCwiaXNzIjoiaHR0cHM6Ly9pZHAucGVwcGVyaS5jb20iLCJhdWQiOlsiaHR0cHM6Ly9pZHAucGVwcGVyaS5jb20vcmVzb3VyY2VzIiwicGVwcGVyaS5hcGludCIsInBlcHBlcmkud2ViYXBwX2FwaSJdLCJjbGllbnRfaWQiOiJwZXBwZXJpLndlYmFwcC5hcHAucGVwcGVyaS5jb20iLCJzdWIiOiIwM2Y4ZTlmOC1kYWE5LTRhMzYtODI4Yy1iNTZlMmM3Mzc0ZDkiLCJhdXRoX3RpbWUiOjE2NDgyMTA0MjMsImlkcCI6ImF6dXJlLXBlcHBlcmkiLCJlbWFpbCI6IlN1cHBvcnRBZG1pblVzZXJfMzAwMTAxMjdAV3JudHkuY29tIiwicGVwcGVyaS5pZCI6MjQwNTAxLCJwZXBwZXJpLnVzZXJ1dWlkIjoiMDNmOGU5ZjgtZGFhOS00YTM2LTgyOGMtYjU2ZTJjNzM3NGQ5IiwicGVwcGVyaS5kaXN0cmlidXRvcmlkIjozMDAxMDEyNywicGVwcGVyaS5kaXN0cmlidXRvcnV1aWQiOiJjYTljODMzNS0yNzFhLTRmNGYtYTc1Zi0zNGJkM2JjNWRmOGIiLCJwZXBwZXJpLmRhdGFjZW50ZXIiOiJwcm9kIiwicGVwcGVyaS5hcGludGJhc2V1cmwiOiJodHRwczovL2FwaW50LnBlcHBlcmkuY29tL3Jlc3RhcGkiLCJwZXBwZXJpLmVtcGxveWVldHlwZSI6MSwicGVwcGVyaS5iYXNldXJsIjoiaHR0cHM6Ly9wYXBpLnBlcHBlcmkuY29tL1YxLjAiLCJwZXBwZXJpLndhY2RiYXNldXJsIjoiaHR0cHM6Ly9jcGFwaS5wZXBwZXJpLmNvbSIsInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJwZXBwZXJpLndlYmFwcF9pZGVudGl0eSIsInBlcHBlcmkucHJvZmlsZSIsInBlcHBlcmkuYXBpbnQiLCJwZXBwZXJpLndlYmFwcF9hcGkiXSwiYW1yIjpbImV4dGVybmFsIl19.B1KGo6PhtlqW-V2enBrmurJZEkDPAHngNzJx_lzc_BbnI1bOjdN6NYvl3oPWaJvBi0erazpuC_LOE7UfE9AEcc2aWD3zWxLgazPkC4cIhEn_iz6hVC5OGRSyRIQfVetmCUvFuVBMT0BuGROYqsWxHFoiMxzuZF35_vsRY455D2HE-aq1M92MrQDoAbic_F1T9ZCEiOK47hRc759VWFe1SfVoOrdi1t_t3zO99gEVRsjcXrXpY-wdba4g8EohTOcfelEfwYNBRHSPeNA2nKZCBsIxH9doN7Uu3Qs4ORRFGfzS4R5oNRMdQV2mC4RZ-Lae79PcBWO_sl0v9LQ7DTJgCg"
headers["X-Pepperi-ConsumerKey"] = "16GmqjAy1Jj3Dbx2RnlntoGGgn5ldtkn"
resp = requests.get(url, headers=headers)

print(resp.status_code)
print(resp.content)