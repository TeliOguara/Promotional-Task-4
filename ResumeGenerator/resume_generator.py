import json
import os

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Template file not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON.")
        return None

def generate_resume(data):
    lines = [
        f"{data['name']}",
        f"{data['email']} | {data['phone']}",
        "-" * 40,
        "Education:"
    ]
    for edu in data.get('education', []):
        lines.append(f"- {edu['degree']} in {edu['field']} from {edu['school']} ({edu['year']})")
    
    lines.append("\nExperience:")
    for job in data.get('experience', []):
        lines.append(f"- {job['title']} at {job['company']} ({job['years']})")
    
    lines.append("\nSkills:")
    lines.append(", ".join(data.get('skills', [])))

    return "\n".join(lines)

def save_resume(content, filename):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Resume saved as {filename}")

def main():
    json_path = input("Enter path to JSON template (e.g., resume_template.json): ").strip()
    data = load_data(json_path)
    if data:
        resume = generate_resume(data)
        output_name = input("Enter output filename (e.g., my_resume.txt): ").strip()
        save_resume(resume, output_name)

if __name__ == "__main__":
    main()
