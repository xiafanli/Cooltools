import re

pattern = '^=[A-Z]+|^$'

negate = True

content = """=ERROR REPORT==== 3-Feb-2016::03:10:32 ===
connection <0.23893.109>, channel 3 - soft error:
{amqp_error,not_found,
            "no queue 'bucket-1' in vhost '/'",
            'queue.declare'}


=ERROR REPORT==== 3-Feb-2016::03:10:32 ===
connection <0.23893.109>, channel 3 - soft error:
{amqp_error,not_found,
            "no queue 'bucket-1' in vhost '/'",
            'queue.declare'}False
"""


def main():
    try:
        regex = re.compile(pattern)
    except Exception, e:
        print("Failed to compile pattern: %s" % e)

    lines = content.split("\n")
    print("match line")
    for line in lines:
        if regex.match(line):
            match = True
        else:
            match = False
        if negate:
            match = not match
        print("%s \t %s" % (match, line))


if __name__ == '__main__':
    main()
