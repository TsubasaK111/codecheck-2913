import pdb, sys

def main(arguments, options):
    for argument in arguments:
        input_number = int(argument)

        number = "1"
        number_block = ""
        for h in xrange(1,input_number):
            for i,v in enumerate(number):
                number_block += v
                if ((i+1) >= len(number)) or not number[i] == number[i+1]:
                    block_expression = str(len(number_block)) + v
                    output_number += block_expression
                else:
                    output_number = "huh?" + i + v
            number = output_number

                #     number_block += v
                # elif len(number_block) > 0:
                #     block_expression = str(len(number_block)) + v
                #     number += block_expression
                # else: number = "11"
                # number += block_expression


            # for digit in enumerate(argument):
            #     numbers.append(digit)
            # previous_digit = 0
            # same_digits = []
            # for digit in numbers:
            #     string = ""
            #     for thing in digit:
            #         string += str(thing)
            #     print string
            #
            #     if int(digit) == int(previous_digit):
            #         same_digits.append(digit)
            #     else:
            #         same_digits_count = len(same_digits)
            #         if same_digits_count>0:
            #             output_numbers.append(same_digits_count)
            #             output_numbers.append(same_digits[0])
            #         same_digits = []
            #     previous_digit = digit
        print number

# def main(arguments, options):
#     numbers = ""
#     for argument in arguments:
#         numbers += argument
#     print numbers
