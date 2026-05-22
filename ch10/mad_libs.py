from pathlib import Path

BASE_DIR = Path.home() / 'Desktop' / 'atbswp' / 'ch10'/ 'mad_libs'

def load_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        return content 

def save_story(file_path, story_content):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(story_content)

def main():
    template_path = BASE_DIR / 'mad_libs_template.txt'

    completed_story_path = BASE_DIR / "completed_story.txt"

    template_text = load_template(template_path)

    words = template_text.split()

    new_story = []

    for word in words:
        clean_word = word.strip('.,!"')
        prompt_type = None

        if clean_word == 'ADJECTIVE':
            prompt_type = 'adjective'

        elif clean_word =='NOUN':
            prompt_type = 'noun'

        elif clean_word =='VERB':
            prompt_type = 'verb'

        elif clean_word =='ADVERB':
            prompt_type = 'adverb'

        if prompt_type is not None:
            user_word = input(f'Enter an {prompt_type}:\n')
            new_story.append(user_word)

        else:
            new_story.append(word)

    new_story_string = ' '.join(new_story)

    save_story(completed_story_path, new_story_string)

if __name__ == "__main__":
    main()