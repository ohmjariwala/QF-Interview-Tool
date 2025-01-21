import requests
import PyPDF2
from bs4 import BeautifulSoup
from io import BytesIO
import re

class QuestionScraper:
    def __init__(self):
        self.pdf_url = "https://academyflex.com/wp-content/uploads/2024/03/a-practical-guide-to-quantitative-finance-interviews.pdf"
        self.quantnet_url = "https://quantnet.com/threads/big-list-of-quant-interview-questions-with-answers.36240/"
        
    def scrape_pdf_questions(self):
        """Scrape questions from the PDF guide."""
        try:
            # Download PDF
            response = requests.get(self.pdf_url)
            pdf_file = BytesIO(response.content)
            
            # Read PDF
            reader = PyPDF2.PdfReader(pdf_file)
            questions = []
            
            # Process each page
            for page in reader.pages:
                text = page.extract_text()
                # Look for question patterns (e.g., "Question:", numbered questions)
                question_matches = re.finditer(r'(?:Question[:\s]|^\d+[\)\.]\s)(.+?)(?=\n|$)', text, re.MULTILINE)
                for match in question_matches:
                    question = match.group(1).strip()
                    if len(question) > 10:  # Filter out very short matches
                        questions.append({
                            "question": question,
                            "source": "Practical Guide to Quantitative Finance",
                            "category": "quant"
                        })
            
            return questions
        except Exception as e:
            print(f"Error scraping PDF: {str(e)}")
            return []

    def scrape_quantnet_questions(self):
        """Scrape questions from QuantNet forum."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(self.quantnet_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            
            questions = []
            # Find post content
            post_content = soup.find('div', class_='message-content')
            if post_content:
                # Split content by newlines and look for question patterns
                lines = post_content.get_text().split('\n')
                current_question = ""
                
                for line in lines:
                    line = line.strip()
                    # Look for numbered questions or question markers
                    if re.match(r'^\d+[\)\.]\s', line) or 'Question:' in line:
                        if current_question:
                            questions.append({
                                "question": current_question,
                                "source": "QuantNet Forum",
                                "category": "quant"
                            })
                        current_question = line
                    elif current_question and line:  # Continue current question
                        current_question += " " + line
                
                # Add the last question
                if current_question:
                    questions.append({
                        "question": current_question,
                        "source": "QuantNet Forum",
                        "category": "quant"
                    })
            
            return questions
        except Exception as e:
            print(f"Error scraping QuantNet: {str(e)}")
            return []

    def get_all_questions(self):
        """Get questions from all sources."""
        questions = []
        questions.extend(self.scrape_pdf_questions())
        questions.extend(self.scrape_quantnet_questions())
        return questions 