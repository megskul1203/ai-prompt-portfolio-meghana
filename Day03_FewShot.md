<img width="1920" height="1020" alt="Email classifier and JSON formatter" src="https://github.com/user-attachments/assets/46fc13c5-720d-42a4-805e-448b3eed7772" />
1. Email Classifiers  
     
   Examples:   
   "Free money \- click here\!" \-\> spam  
   "Buy Viagra now\!" \-\> spam  
   "Team meeting at 3 pm?" \-\> not spam  
     
   Classify these emails( respond spam/not spam only):  
     
   1\. "Your invoice \#1234 is ready for payment"  
   2\. "WIN iPhone \- claim now\!"  
   3\. "Project update call tomorrow at 2 pm"  
   4\. "Limited time: 90% off everything\!"  
   5\. "Re: Budget approval discussion"  
     
     
   Response:   
     
1. not spam  
2. spam  
3. not spam  
4. spam  
5. not spam

2. JSON Formatter  
     
   Examples:   
   Input: Apple price 100  
   Output: {"item": "Apple", "price":100}  
   Input: Banana price 50  
   Output: {"item": "Banana", "price":50}  
   Format these exact JSON format:  
   1\. Orange price 75  
   2\. Mango price 120  
   3\. Kiwi price 200  
     
   Response:  
     
   	{"item": "Orange", "price":75}  
   	{"item": "Mango", "price":120}  
   	{"item": "Kiwi", "price":200}  
     
3. Tone Converter  
     
   Example:  
   Input: "You're late again"  
   Output: "I notice you arrived later than the scheduled time"  
   Input: " This report sucks"  
   Output: "This report needs some improvements"  
     
   Convert to professional tone:   
   1\. "Fix this bud immediately"  
   2\. "Your code is terrible"  
   3\. "Where's my coffee?"  
     
   Response:  
1. “Please address this issue as soon as possible.”  
2. “Your code needs significant improvement.”  
3. “Could you please let me know where my coffee is?”

4. Headline Generator  
     
   Examples:  
   "AI improves productivity" → "AI Tools Boost Team Productivity 35%"  
   "Python learning course" → "Master Python in 30 Days: Complete Guide"   
   "Remote work benefits" → "Why Remote Work Wins: Top 5 Benefits"  
     
   Generate headlines for:  
   1\. "Prompt engineering tutorial"  
   2\. "Data science career path"  
   3\. "ChatGPT productivity hacks"  
     
   Response:  
     
1. Prompt Engineering Made Easy: Step-by-Step Tutorial for Beginners  
2. Data Science Career Path: Skills, Roles, and Salary Roadmap  
3. ChatGPT Productivity Hacks: 10 Tips to Save Hours Every Day

5. Travel Itinerary  
     
   Examples:  
   "Delhi 2 days" → "Day 1: Red Fort, Chandni Chowk. Day 2: Qutub Minar, India Gate"  
   "Goa 3 days" → "Day 1: Baga Beach. Day 2: Old Goa churches. Day 3: Dudhsagar Falls"  
     
   Create itinerary: "Mumbai 2 days"  
     
   Response:  
     
   "Mumbai 2 days" → Day 1: Gateway of India, Marine Drive, Colaba Causeway. Day 2: Elephanta Caves, Bandra Bandstand, Juhu Beach
