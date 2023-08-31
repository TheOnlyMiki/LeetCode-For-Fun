class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        space = 0
        count = 0
        record_last_line = []
        output = []

        for i, word in enumerate(words):
            length = len(word)

            # Already have + current word + spaces of ' ' needs
            if count + length + space > maxWidth:
                # Find out the remaining spaces
                remain_space = maxWidth - count
                pre_line = ""

                # Make line - if there is only one word in line handle by EXCEPT
                try:
                    # Calculate the needs of spaces and if there is addition necessary
                    # If there is 6 remain spaces, and there is 3 words (which is mean 
                    # a least need 3 spaces if there is new word is joining), so 6 / 
                    # (3 - 1) = 6 / 2, cause there is only 2 spaces between 3 words.
                    space_needs = remain_space // (space-1)
                    addition_space = remain_space % (space-1)
                    # Create a space of " " then join together
                    pre_line = str((" " * space_needs).join( words[ i-space : i ] ))
                    # Get the first index for insert space if necessary
                    remain_space = record_last_line[0]
                    for index in range(addition_space):
                        pre_line = pre_line[:remain_space] + " " + pre_line[remain_space:]
                        remain_space += record_last_line[index+1] + space_needs + 1
                # Handle the Case - Only one word in last line
                except:
                    pre_line = str(words[i-1] + " " * remain_space)

                # Store the complete result of last line
                output.append(pre_line)
                #Initial for next iteration
                record_last_line = []
                space = count = 0

            # Iteration update
            record_last_line.append(length)
            count += length
            space += 1

        # Handle the last line
        last_line = str( " ".join(words[-space:]) )
        remain_space = maxWidth - len(last_line)
        output.append(last_line + " " * remain_space)

        return output
