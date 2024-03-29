# PROBLEM
"""

Let A be an <b>affine</b> <b>plane</b> over a <b>radically</b> <b>integral</b> <b>local</b> <b>field</b> F with residual characteristic p.

We consider an <b>open</b> <b>oriented</b> <b>line</b> <b>section</b> U of A with normalized Haar measure m.

Define f(m, p) as the maximal possible discriminant of the <b>jacobian</b> associated to the <b>orthogonal</b> <b>kernel</b> <b>embedding</b> of U into A.

Find f(20230401, 57). Give as your answer the concatenation of the first letters of each bolded word.

"""


def f(m, p):
    text = """Let A be an <b>affine</b> <b>plane</b> over a <b>radically</b> <b>integral</b> <b>local</b> <b>field</b> F with residual characteristic p.

We consider an <b>open</b> <b>oriented</b> <b>line</b> <b>section</b> U of A with normalized Haar measure m.

Define f(m, p) as the maximal possible discriminant of the <b>jacobian</b> associated to the <b>orthogonal</b> <b>kernel</b> <b>embedding</b> of U into A.

Find f(20230401, 57). Give as your answer the concatenation of the first letters of each bolded word."""
    tokens = text.split("<b>")
    tokens_with_ending_bold_tag = list(filter(lambda token: "</b>" in token, tokens))
    first_characters = list(map(lambda token: token[0], tokens_with_ending_bold_tag))
    answer = "".join(first_characters)
    return answer


if __name__ == "__main__":
    answer = f(20230401, 57)
    print(answer)
