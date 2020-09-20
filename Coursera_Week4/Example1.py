def double_word(word):
    result = (word * 2)
    final_result = result + str(len(result))
    return final_result

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0