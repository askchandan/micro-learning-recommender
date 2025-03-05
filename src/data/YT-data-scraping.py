import requests
import csv
import concurrent.futures
import time
from typing import List, Dict

class YouTubeScraper:
    def __init__(self, api_keys: List[str]):
        # Multiple API keys to rotate
        self.API_KEYS = api_keys
        self.current_key_index = 0

        # Comprehensive skills list with multiple search variations
        self.skills = [
            {"query": "HTML & CSS", "variations": [
                "HTML CSS tutorial", 
                "Web development HTML CSS", 
                "Complete HTML CSS course"
            ]},
            {"query": "JavaScript Basics", "variations": [
                "JavaScript tutorial for beginners", 
                "Complete JavaScript course",
                "JavaScript programming fundamentals"
            ]},
            {"query": "React.js", "variations": [
                "React.js full course", 
                "React tutorial for beginners",
                "Learn React programming"
            ]},
            {"query": "Angular.js", "variations": [
                "Angular.js tutorial", 
                "Angular full course",
                "Angular for web development"
            ]},
            {"query": "Vue.js", "variations": [
                "Vue.js tutorial", 
                "Vue.js full course",
                "Vue.js for beginners"
            ]},
            {"query": "Node.js", "variations": [
                "Node.js tutorial", 
                "Node.js full course",
                "Backend development with Node.js"
            ]},
            {"query": "Express.js", "variations": [
                "Express.js tutorial", 
                "Express.js full course",
                "Backend API with Express.js"
            ]},
            {"query": "Django for Web Dev", "variations": [
                "Django tutorial", 
                "Django full course",
                "Python web development with Django"
            ]},
            {"query": "Flask Web Development", "variations": [
                "Flask tutorial", 
                "Flask full course",
                "Python web development with Flask"
            ]},
            {"query": "PHP & Laravel", "variations": [
                "PHP Laravel tutorial", 
                "Laravel full course",
                "Web development with PHP Laravel"
            ]},
            {"query": "MERN Stack", "variations": [
                "MERN stack tutorial", 
                "Full stack MERN development",
                "Complete MERN stack course"
            ]},
            {"query": "MEAN Stack", "variations": [
                "MEAN stack tutorial", 
                "Full stack MEAN development",
                "Complete MEAN stack course"
            ]},
            {"query": "Full Stack with Python & Django", "variations": [
                "Python full stack tutorial", 
                "Django full stack development",
                "Complete Python web development course"
            ]},
            {"query": "Full Stack with Java & Spring Boot", "variations": [
                "Java full stack tutorial", 
                "Spring Boot full stack development",
                "Complete Java web development course"
            ]},
            {"query": "REST API Development", "variations": [
                "REST API tutorial", 
                "REST API full course",
                "Web API development"
            ]},
            {"query": "GraphQL APIs", "variations": [
                "GraphQL tutorial", 
                "GraphQL API development",
                "Modern API design with GraphQL"
            ]},
            {"query": "Microservices Architecture", "variations": [
                "Microservices tutorial", 
                "Microservices architecture course",
                "Distributed systems design"
            ]},
            {"query": "Generative AI Basics", "variations": [
                "Generative AI tutorial", 
                "Introduction to Generative AI",
                "Generative AI for beginners"
            ]},
            {"query": "GPT & Large Language Models", "variations": [
                "GPT tutorial", 
                "Large Language Models explained",
                "AI language models course"
            ]},
            {"query": "AI Image Generation", "variations": [
                "AI image generation tutorial", 
                "Generative AI for images",
                "Machine learning image creation"
            ]},
            {"query": "AI Video Generation", "variations": [
                "AI video generation tutorial", 
                "Generative AI for video",
                "Machine learning video creation"
            ]},
            {"query": "AI in Coding", "variations": [
                "AI coding assistant", 
                "AI for software development",
                "Machine learning in programming"
            ]},
            {"query": "LangChain for AI Apps", "variations": [
                "LangChain tutorial", 
                "Building AI apps with LangChain",
                "LangChain full course"
            ]},
            {"query": "Fine-Tuning LLMs", "variations": [
                "LLM fine-tuning tutorial", 
                "Large Language Model customization",
                "Advanced AI model training"
            ]},
            {"query": "Machine Learning Basics", "variations": [
                "Machine Learning tutorial", 
                "Machine Learning for beginners",
                "Introduction to Machine Learning"
            ]},
            {"query": "Deep Learning with TensorFlow", "variations": [
                "TensorFlow tutorial", 
                "Deep Learning with TensorFlow",
                "Neural networks TensorFlow course"
            ]},
            {"query": "Deep Learning with PyTorch", "variations": [
                "PyTorch tutorial", 
                "Deep Learning with PyTorch",
                "Neural networks PyTorch course"
            ]},
            {"query": "Computer Vision", "variations": [
                "Computer Vision tutorial", 
                "Machine Learning Computer Vision",
                "Image processing AI course"
            ]},
            {"query": "NLP", "variations": [
                "Natural Language Processing tutorial", 
                "NLP with Python",
                "Text analysis AI course"
            ]},
            {"query": "Data Science with Python", "variations": [
                "Python Data Science tutorial", 
                "Data Science full course",
                "Data analysis with Python"
            ]},
            {"query": "Data Science with R", "variations": [
                "R Data Science tutorial", 
                "Data Science with R",
                "Statistical analysis R course"
            ]},
            {"query": "Feature Engineering", "variations": [
                "Feature Engineering tutorial", 
                "Machine Learning feature selection",
                "Data preparation course"
            ]},
            {"query": "AI Ethics & Bias", "variations": [
                "AI Ethics tutorial", 
                "Ethical AI development",
                "Bias in Machine Learning"
            ]},
            {"query": "Excel for Data Analysis", "variations": [
                "Excel data analysis tutorial", 
                "Excel for business intelligence",
                "Advanced Excel course"
            ]},
            {"query": "Power BI", "variations": [
                "Power BI tutorial", 
                "Data visualization Power BI",
                "Business intelligence Power BI"
            ]},
            {"query": "Tableau", "variations": [
                "Tableau tutorial", 
                "Data visualization Tableau",
                "Tableau for data analysis"
            ]},
            {"query": "SQL for Data Analysis", "variations": [
                "SQL tutorial", 
                "SQL for data analysis",
                "Database querying course"
            ]},
            {"query": "Data Cleaning with Pandas", "variations": [
                "Pandas data cleaning", 
                "Data preprocessing Python",
                "Pandas tutorial for data science"
            ]},
            {"query": "Exploratory Data Analysis", "variations": [
                "Exploratory Data Analysis tutorial", 
                "EDA with Python",
                "Data visualization and analysis"
            ]},
            {"query": "Google Data Studio", "variations": [
                "Google Data Studio tutorial", 
                "Data visualization Google Studio",
                "Business intelligence reporting"
            ]},
            {"query": "Business Intelligence", "variations": [
                "Business Intelligence tutorial", 
                "BI data analysis",
                "Enterprise data strategy"
            ]},
            {"query": "CPU & GPU Architecture", "variations": [
                "CPU GPU architecture", 
                "Computer hardware tutorial",
                "Advanced computer architecture"
            ]},
            {"query": "Computer Networking Basics", "variations": [
                "Computer networking tutorial", 
                "Network fundamentals",
                "Networking for beginners"
            ]},
            {"query": "Embedded Systems Programming", "variations": [
                "Embedded systems tutorial", 
                "Microcontroller programming",
                "Embedded software development"
            ]},
            {"query": "IoT Hardware & Development", "variations": [
                "IoT tutorial", 
                "Internet of Things development",
                "IoT hardware programming"
            ]},
            {"query": "FPGA & Microcontrollers", "variations": [
                "FPGA tutorial", 
                "Microcontroller programming",
                "Digital hardware design"
            ]},
            {"query": "Computer Repair & Troubleshooting", "variations": [
                "Computer repair tutorial", 
                "PC troubleshooting guide",
                "Hardware maintenance course"
            ]},
            {"query": "Linux System Administration", "variations": [
                "Linux administration tutorial", 
                "Linux system management",
                "Linux server administration"
            ]}
        ]

    def rotate_api_key(self):
        """
        Rotate to the next API key
        """
        self.current_key_index = (self.current_key_index + 1) % len(self.API_KEYS)
        return self.API_KEYS[self.current_key_index]

    def search_youtube(self, query: str, max_results: int = 20) -> List[Dict]:
        """
        Search YouTube using Official YouTube Data API v3 with key rotation
        """
        videos = []
        attempts = 0
        max_attempts = len(self.API_KEYS) * 2  # Prevent infinite loops

        while attempts < max_attempts:
            try:
                # Use current API key
                current_key = self.API_KEYS[self.current_key_index]

                # YouTube Data API v3 search endpoint
                search_url = "https://www.googleapis.com/youtube/v3/search"
                
                # Parameters for video search
                params = {
                    'part': 'snippet',
                    'q': query,
                    'type': 'video',
                    'maxResults': max_results,
                    'key': current_key
                }
                
                # Send request
                response = requests.get(search_url, params=params)
                
                # Check response
                if response.status_code == 200:
                    search_results = response.json()
                    
                    # Process each video
                    for item in search_results.get('items', []):
                        video_id = item['id']['videoId']
                        
                        # Get video details
                        video_details_url = "https://www.googleapis.com/youtube/v3/videos"
                        video_params = {
                            'part': 'contentDetails,statistics',
                            'id': video_id,
                            'key': current_key
                        }
                        
                        video_response = requests.get(video_details_url, params=video_params)
                        
                        if video_response.status_code == 200:
                            video_info = video_response.json()
                            
                            # Extract video length
                            try:
                                import isodate
                                duration = video_info['items'][0]['contentDetails']['duration']
                                length_seconds = isodate.parse_duration(duration).total_seconds()
                            except Exception:
                                length_seconds = 0
                            
                            # Filter videos between 5 and 60 minutes
                            if 300 <= length_seconds <= 3600:
                                video = {
                                    'video_title': item['snippet']['title'],
                                    'length': f"{int(length_seconds)} seconds",
                                    'skill_category': query,
                                    'url': f"https://youtu.be/{video_id}"
                                }
                                videos.append(video)
                        
                        # Add small delay to respect API rate limits
                        time.sleep(0.2)
                    
                    # Successfully retrieved videos
                    return videos[:20]
                
                # Handle quota exceeded
                elif response.status_code == 403:
                    print(f"Quota exceeded for key {current_key}. Rotating to next key.")
                    self.rotate_api_key()
                    attempts += 1
                    time.sleep(1)  # Small delay before retry
                else:
                    print(f"Error searching for {query}: {response.text}")
                    break
            
            except Exception as e:
                print(f"Exception in search_youtube for {query}: {e}")
                self.rotate_api_key()
                attempts += 1
                time.sleep(1)
        
        return videos

    def scrape_all_skills(self, max_workers: int = 5) -> List[Dict]:
        """
        Scrape videos for all skills using concurrent processing
        """
        all_videos = []
        
        # Use multiple search queries for each skill
        search_queries = []
        for skill in self.skills:
            search_queries.extend(skill['variations'])
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Map skills to search function
            future_to_query = {
                executor.submit(self.search_youtube, query): query 
                for query in search_queries
            }
            
            # Collect results
            for future in concurrent.futures.as_completed(future_to_query):
                query = future_to_query[future]
                try:
                    videos = future.result()
                    all_videos.extend(videos)
                    print(f"Scraped {len(videos)} videos for {query}")
                except Exception as e:
                    print(f"Error scraping {query}: {e}")
        
        return all_videos

    def save_to_csv(self, videos: List[Dict], filename: str = 'youtube_technical_skills1_videos.csv'):
        """
        Save scraped videos to CSV
        """
        # Remove duplicates
        unique_videos = list({v['url']: v for v in videos}.values())
        
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['video_title', 'length', 'skill_category', 'url'])
            writer.writeheader()
            writer.writerows(unique_videos)
        
        print(f"Saved {len(unique_videos)} unique videos to {filename}")

def main():
    # List of multiple API keys
    API_KEYS = [
        # now expired these ones.
        'AIzaSyD0X6Yogb46joEmNHaSy6swPZ9RKsWmkBQ',
        'AIzaSyAPA78IbKrS4KCR48Xt6YFd3gxQCkEpUyg',
        'AIzaSyDDfy-2SOPkYSeFX0eyG4N_RStw-d6L7UQ'  # Add more keys
    ]
    # Initialize scraper with multiple keys
    scraper = YouTubeScraper(API_KEYS)
    
    # Scrape videos
    videos = scraper.scrape_all_skills()
    
    # Save to CSV
    scraper.save_to_csv(videos)

if __name__ == "__main__":
    main()

