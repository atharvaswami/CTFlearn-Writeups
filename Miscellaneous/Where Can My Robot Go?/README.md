<h2>Where Can My Robot Go?</h2>

<h4>Problem Statement:</h4>
<p>Where do robots find what pages are on a website?</p>
<p>Hint: What does disallow tell a robot?</p>

<h4>Step-1:</h4>
<p>A robots.txt file tells search engine crawlers which pages or files the crawler can or can't request from your site. So go to the url <a>https://ctflearn.com/robots.txt</a> to get some hint.</p>

<h4>Step-2:</h4>
<p>The output seen is:</p>
<p><pre>
User-agent: *
Disallow: /70r3hnanldfspufdsoifnlds.html
</pre></p>

<h4>Step-3:</h4>
<p>Now go to the url <a>https://ctflearn.com/70r3hnanldfspufdsoifnlds.html</a> where you will find the flag.</p>

<h4>Step-4:</h4>
<p>The flag found on the above webpage is <code>CTFlearn{r0b0ts_4r3_th3_futur3}</code></p>
