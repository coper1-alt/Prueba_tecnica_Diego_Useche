from playwright.sync_api import sync_playwright
import os

def html_to_pdf(html_path, pdf_path):
    """Convert HTML file to PDF using Playwright"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Load the HTML file
        page.goto(f"file:///{os.path.abspath(html_path)}", wait_until='networkidle')
        
        # Generate PDF with adjusted settings
        page.pdf(
            path=pdf_path,
            format='A4',
            print_background=True,
            scale=0.8,  # Scale down to 80% to fit better
            margin={
                'top': '0.5cm',
                'right': '0.5cm',
                'bottom': '0.5cm',
                'left': '0.5cm'
            }
        )
        
        browser.close()
    
    print(f"PDF created successfully: {pdf_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2:
        html_file = sys.argv[1]
        if len(sys.argv) >= 3:
            pdf_file = sys.argv[2]
        else:
            pdf_file = html_file.replace('.html', '.pdf')
    else:
        print("Usage: python html_to_pdf.py <input.html> [output.pdf]")
        sys.exit(1)
    
    html_to_pdf(html_file, pdf_file)
