
Motivation and Background (10 Points):

My motivation for this project stemmed from an initial difficulty in identifying a suitable project idea. This challenge led me to consider the process of project ideation itself, particularly the first step: identifying a problem to solve. This reflection inspired the concept of creating a project that addresses the very issue of finding problems. To tackle this meta-problem, I developed a streamlined web app that aggregates negative Amazon reviews of leading products in a given category and then utilizes ChatGPT to summarize them.

Comparison with Standard ChatGPT (10 Points):

The key difference between my web app and using standard ChatGPT lies in transparency and source credibility. My app mitigates the "black box" effect by explicitly citing the reviews it analyzes. Standard ChatGPT might provide generalized insights on product issues based on its training, whereas my app offers summaries of actual customer feedback. By employing GPT solely for language summarization and not as the primary research tool, and by including citations, the results become more reliable and trustworthy. Aside from being more trustworthy, as all sources of information were cited, it also has the ability to change parameters to filter for a specific niche of review. In the code base the ASIN api call is given a set of parameters to get the best reviews. I choose not to add them to the web app because I wanted to make it as sleek and simple as possible. 

Project Story and Challenges (15 Points):

Initially, my project concept was overly ambitious due to a lack of thorough research into data sources. My first plan was to scrape data directly from Amazon, but I quickly encountered Amazon's robust security features. I then pivoted to using an API, but its rate limit significantly altered my project's scope. I decided to concentrate on analyzing reviews for a single product. After establishing the data collection process, I integrated the results with the GPT API, developed the application using Streamlit, and uploaded it to GitHub. I had minor issues with the flow of the streamlit website but I was able to read documentation and sort the issues out. The APIs caused some frustrating issues as my free trials ran out for both at separate times in dev (while they were wrapped in try except statements) so it was a frustrating issue to find. After it was found fixing it was a easy as loading a few dollars in each account.

Demo of Final Work (15 Points):

https://youtu.be/Wfy6ixLN1Bc

Achievement of Metrics (10 Points):

While my product did not fully meet the initial metrics, I attribute this more to the ambitious nature of these metrics rather than to any shortcomings in my work. The pivot from web scraping to using an API required a significant change in approach. Despite this, I am pleased with the final product, which is both useful and unique. In terms of the metrics I set earliery in terms of runtime being under 30 minutes it far suprasseed this, but that's because the scope of the problem got smaller. Rather than returning 50 results about all products, it just returns around 5 about one problem. The runtime is around 30 seconds to a minute, with the large majority of it spent on the ASIN api call. 

Description of Future Work (10 Points):

I do not currently plan to continue this project, as I am currently occupied with another. However, hypothetically, if I were to proceed, the next step would involve sourcing review data more effectively. The current API is slow and does not fully meet the project's needs. Options might include attempting to bypass Amazon's security measures for scraping data or exploring access to Amazon's reviews through their developer API, though this would likely be contingent on creating a product for Amazon.

Reflection on Learning (10 Points):

This project enhanced my skills in using Streamlit, APIs, and general programming. It also deepened my understanding of how AI can be made more trustworthy, such as by having language models like GPT cite their direct information sources.  Personally I think the main thing holding AI solution back is the fear of an untrustworthy seemingly random black box. We trust AI to do task with low consequence for failure, but cannot trust it to do anything consequential as we do not know its full process for arriving at decisions. Generally I think that taking steps towards offering a look into the black box is essential if use of AI is to become more widespread.






