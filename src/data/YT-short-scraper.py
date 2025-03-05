import requests
import csv
import json
import concurrent.futures
import time
import random
from typing import List, Dict

class UltraDetailedYouTubeScraper:
    def __init__(self, api_keys: List[str]):
        self.API_KEYS = api_keys
        self.current_key_index = 0

        # Comprehensive skills list with ultra-detailed search variations
        self.skills = [
            # Web Development Fundamentals
            {"query": "HTML & CSS", "variations": [
                "HTML CSS beginner crash course", 
                "Web development HTML CSS from scratch", 
                "Complete responsive web design tutorial",
                "HTML CSS modern web development techniques",
                "Zero to hero HTML and CSS mastery"
            ]},
            {"query": "JavaScript Basics", "variations": [
                "JavaScript fundamentals for absolute beginners", 
                "Modern JavaScript programming deep dive",
                "JavaScript ES6+ complete guide",
                "Practical JavaScript coding techniques",
                "JavaScript interview preparation tutorial"
            ]},
            
            # Frontend Frameworks
            {"query": "React.js", "variations": [
                "React.js comprehensive beginner guide", 
                "Modern React development with hooks",
                "React.js project-based learning",
                "Advanced React.js state management",
                "React.js best practices and design patterns"
            ]},
            {"query": "Angular.js", "variations": [
                "Angular.js complete zero to hero tutorial", 
                "Modern Angular development techniques",
                "Angular.js enterprise application development",
                "Angular.js performance optimization",
                "Full stack development with Angular"
            ]},
            {"query": "Vue.js", "variations": [
                "Vue.js ultimate beginner course", 
                "Vue.js 3 comprehensive guide",
                "Vue.js advanced state management",
                "Vue.js real-world application development",
                "Vue.js best practices and design patterns"
            ]},
            
            # Backend Development
            {"query": "Node.js", "variations": [
                "Node.js complete backend development", 
                "Modern Node.js with Express.js",
                "Node.js scalable backend architecture",
                "Node.js microservices tutorial",
                "Enterprise Node.js application development"
            ]},
            {"query": "Express.js", "variations": [
                "Express.js comprehensive API development", 
                "Advanced Express.js routing techniques",
                "Express.js with authentication and security",
                "Express.js performance optimization",
                "Real-world Express.js backend projects"
            ]},
            
            # Python Web Frameworks
            {"query": "Django for Web Dev", "variations": [
                "Django complete web development course", 
                "Django advanced project structure",
                "Django REST framework tutorial",
                "Full stack web development with Django",
                "Django best practices and advanced techniques"
            ]},
            {"query": "Flask Web Development", "variations": [
                "Flask comprehensive web development", 
                "Flask microservices architecture",
                "Advanced Flask application design",
                "Flask with SQLAlchemy and databases",
                "Production-ready Flask applications"
            ]},
            
            # Full Stack Technologies
            {"query": "MERN Stack", "variations": [
                "MERN stack complete full-stack course", 
                "Modern MERN stack development techniques",
                "Full stack MERN application from scratch",
                "MERN stack enterprise-level project",
                "Advanced MERN stack architecture"
            ]},
            {"query": "MEAN Stack", "variations": [
                "MEAN stack comprehensive tutorial", 
                "Full stack MEAN development techniques",
                "Enterprise MEAN stack application design",
                "MEAN stack advanced state management",
                "Real-world MEAN stack projects"
            ]},
            
            # AI and Machine Learning
            {"query": "Generative AI Basics", "variations": [
                "Generative AI comprehensive introduction", 
                "Hands-on generative AI techniques",
                "Generative AI ethical considerations",
                "Advanced generative AI model training",
                "Practical generative AI applications"
            ]},
            {"query": "Machine Learning Basics", "variations": [
                "Machine learning from zero to advanced", 
                "Practical machine learning techniques",
                "Machine learning algorithm deep dive",
                "Machine learning project-based learning",
                "Advanced machine learning strategies"
            ]},
            {"query": "Deep Learning with TensorFlow", "variations": [
                "TensorFlow comprehensive deep learning", 
                "Advanced neural network design",
                "TensorFlow practical implementation",
                "Deep learning complex model architectures",
                "TensorFlow advanced optimization techniques"
            ]},
            
            # Data Science and Analysis
            {"query": "Data Science with Python", "variations": [
                "Python data science complete roadmap", 
                "Advanced data science techniques",
                "Data science real-world project tutorial",
                "Python data analysis comprehensive guide",
                "Professional data science workflow"
            ]},
            {"query": "Exploratory Data Analysis", "variations": [
                "EDA comprehensive techniques", 
                "Advanced data visualization methods",
                "Python data analysis deep dive",
                "Professional EDA workflow",
                "Data science storytelling techniques"
            ]},
            
            # Cloud and DevOps
            {"query": "Computer Networking Basics", "variations": [
                "Comprehensive computer networking tutorial", 
                "Network protocols deep dive",
                "Advanced networking techniques",
                "Network security fundamental course",
                "Modern network infrastructure design"
            ]},
            {"query": "Linux System Administration", "variations": [
                "Linux administration complete guide", 
                "Advanced Linux system management",
                "Linux server deployment techniques",
                "Enterprise Linux infrastructure",
                "Linux security and performance optimization"
            ]}
        ]

    def rotate_api_key(self):
        """Rotate through available API keys"""
        self.current_key_index = (self.current_key_index + 1) % len(self.API_KEYS)
        return self.API_KEYS[self.current_key_index]

    def search_youtube(self, query: str, max_results: int = 100) -> List[Dict]:
        """
        Perform ultra-detailed search on YouTube
        """
        videos = []
        attempts = 0
        max_attempts = len(self.API_KEYS) * 3

        # Multiple search order strategies
        order_types = ['relevance', 'viewCount', 'rating', 'date']

        while attempts < max_attempts:
            try:
                current_key = self.API_KEYS[self.current_key_index]
                search_order = order_types[attempts % len(order_types)]

                search_url = "https://www.googleapis.com/youtube/v3/search"
                
                params = {
                    'part': 'snippet',
                    'q': query + " tutorial in-depth",
                    'type': 'video',
                    'maxResults': max_results,
                    'key': current_key,
                    'order': search_order,
                    'videoDuration': 'medium'
                }
                
                response = requests.get(search_url, params=params)
                
                if response.status_code == 200:
                    search_results = response.json()
                    
                    for item in search_results.get('items', []):
                        video_id = item['id']['videoId']
                        
                        # Get detailed video information
                        video_details_url = "https://www.googleapis.com/youtube/v3/videos"
                        video_params = {
                            'part': 'contentDetails,statistics',
                            'id': video_id,
                            'key': current_key
                        }
                        
                        video_response = requests.get(video_details_url, params=video_params)
                        
                        if video_response.status_code == 200:
                            video_info = video_response.json()
                            
                            try:
                                import isodate
                                duration = video_info['items'][0]['contentDetails']['duration']
                                length_seconds = isodate.parse_duration(duration).total_seconds()
                            except Exception:
                                length_seconds = 0
                            
                            # Strict filter: videos between 5 and 20 minutes
                            if 300 <= length_seconds <= 1200:
                                video = {
                                    'video_title': item['snippet']['title'],
                                    'channel': item['snippet']['channelTitle'],
                                    'length': f"{int(length_seconds)} seconds",
                                    'skill_category': query,
                                    'published_at': item['snippet']['publishedAt'],
                                    'url': f"https://youtu.be/{video_id}"
                                }
                                
                                # Additional statistics
                                try:
                                    stats = video_info['items'][0]['statistics']
                                    video.update({
                                        'views': stats.get('viewCount', 0),
                                        'likes': stats.get('likeCount', 0)
                                    })
                                except Exception:
                                    pass
                                
                                videos.append(video)
                        
                        time.sleep(0.1)
                    
                    if len(videos) >= max_results:
                        break
                
                elif response.status_code == 403:
                    print(f"Quota exceeded. Rotating to next key.")
                    self.rotate_api_key()
                    attempts += 1
                    time.sleep(1)
                else:
                    print(f"Error searching for {query}: {response.text}")
                    break
            
            except Exception as e:
                print(f"Exception in search_youtube for {query}: {e}")
                self.rotate_api_key()
                attempts += 1
                time.sleep(1)
        
        return videos

    def scrape_all_skills(self, max_workers: int = 15) -> List[Dict]:
        """
        Scrape videos for all skills using concurrent processing
        """
        all_videos = []
        
        # Expand search queries
        search_queries = []
        for skill in self.skills:
            search_queries.extend(skill['variations'])
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Randomize search order
            random.shuffle(search_queries)
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

    def save_to_csv(self, videos: List[Dict], filename: str = 'ultra_detailed_tech_videos.csv'):
        """
        Save scraped videos to CSV with comprehensive information
        """
        # Remove duplicates while preserving order
        unique_videos = list({v['url']: v for v in videos}.values())
        
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=[
                'video_title', 'channel', 'length', 
                'skill_category', 'published_at', 
                'url', 'views', 'likes'
            ])
            writer.writeheader()
            writer.writerows(unique_videos)
        
        print(f"Saved {len(unique_videos)} unique videos to {filename}")

def main():
    # Replace with your actual YouTube Data API keys
    API_KEYS = [
        'AIzaSyBZjBr6VRfoyJZ4sDGbA-7qGZQZCSLFiGk',
        'AIzaSyCEnG5MLoLmY7jNVwh7d-Vwf5uunBAV3Xg',
        'AIzaSyD3yRQEpBhSbLuqXdsBpnEQLPddm00yPGU'
    ]
    
    # Initialize scraper with multiple keys
    scraper = UltraDetailedYouTubeScraper(API_KEYS)
    
    # Scrape videos
    videos = scraper.scrape_all_skills()
    
    # Save to CSV
    scraper.save_to_csv(videos)

if __name__ == "__main__":
    main()
