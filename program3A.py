def is_palindrome(s: str) -> bool:
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned_str == cleaned_str[::-1]

string = "A man, a plan, a canal, Panama"
print(is_palindrome(string))  