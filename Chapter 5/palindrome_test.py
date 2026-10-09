def is_palindrome(text):
    
    cleaned = ""
    for character in text:
        
            cleaned += character.lower()

    
    stack = []
    for character in cleaned:
        stack.append(character)

    
