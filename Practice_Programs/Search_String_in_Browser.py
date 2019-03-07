import re    
src = driver.page_source
text_found = re.search(r'text_to_search', src)