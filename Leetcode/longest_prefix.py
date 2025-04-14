# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
def longest_common_prefix(strs):
    if not strs:
        return ""

    # Start with the first string as the prefix
    prefix = strs[0]

    # Compare the prefix with each string
    for s in strs[1:]:
        # Shorten the prefix until it matches the start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix