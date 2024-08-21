import requests

def get_domain_category(domain):
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    
    headers = {
        "accept": "application/json",
        "x-apikey": "API_KEY"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        # Extract category from the response
        category = data.get('data', {}).get('attributes', {}).get('categories', [])
        return category
    else:
        return f"Error: {response.status_code}"

def process_domains_from_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        domains = file.readlines()
    
    with open(output_filename, 'w') as file:
        for domain in domains:
            domain = domain.strip()  # Remove any leading/trailing whitespace
            if domain:
                category = get_domain_category(domain)
                file.write(f"Domain: {domain}\n")
                file.write(f"Category: {category}\n\n")

# Provide the input and output filenames
input_filename = "domains.txt"
output_filename = "results.txt"
process_domains_from_file(input_filename, output_filename)
