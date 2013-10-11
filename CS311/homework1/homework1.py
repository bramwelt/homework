"""
CS311 - Homework 1

This file holds the collected functions for questions 1-4 of homework
1 for CS311-FA13.

:author: Trevor Bramwell
"""
from os import (access, chdir, error, getcwd, mkdir, makedirs, path,
                sep, symlink, F_OK, W_OK)

class Main(object):
    """
    Holds answers/functions for all the questions.
    """

    def question1(self, term, course):
        """
        Creates a directory `./<term>/<course>/` that contains the
        subdirectories: 
            assignment, examples, exams, lecture_notes, submissions 
        and the symlinks:
            handin -> /usr/local/classes/eecs/<term>/<course>/handin
            website -> /usr/local/classes/eecs/<term>/<course>/public_html

        Fulfills requirements for question 1.

        :arg term: The term of the school year
        :arg course: Name of a course. Generally in the form:
                     [A-Z]{2}[0-9]{3}
        """
        verbose = False
        # Paths for <term>/<course>/ and symlink source.
        course_path = path.join(getcwd(), term, course)
        # symlink paths
        symlink_base_path = path.join(sep, 'usr', 'local', 'classes', 'eecs')
        symlink_source_path = path.join(symlink_base_path, term, course)
        handin_path = path.join(symlink_source_path, 'handin')
        website_path = path.join(symlink_source_path, 'website')
        # Directories to create for a course
        course_dirs = ['assignments', 'examples', 'exams', 'lecture_notes',
                       'submissions']
        course_flags = F_OK | W_OK
        
        def created_dir(directory):
            print "Create directory: {0}".format(directory)

        # Ensure the directory doesn't exist before creating it.
        if not path.exists(course_path):
            makedirs(course_path)
            if verbose:
                created_dir(course_path)
        elif not path.isdir(course_path):
            raise error("Course path '{0}' exists, "
                        "but is not a directory".format(course_path))
        elif not access(course_path, course_flags):
            raise error("You do not have permissions to create "
                        "directories in: {0}".format(course_path))

        if path.exists(course_path):
            chdir(course_path)
            for course in course_dirs:
                if not path.exists(course):
                    mkdir(course)
            if path.exists(symlink_base_path):
                symlink(handin_path, 'handin')
                symlink(website_path, 'website')
            elif not access(symlink_base_path, W_OK):
                raise error("Can't create symlinks 'handin' or "
                            "'website'. You do not have access to: "
                            "{0}".format(symlink_base_path))
            else:
                raise error("Not symlinking 'handing' or 'website' as "
                            "you don't seem to be on os-class. "
                            "Path does not exist: "
                            "{0}".format(symlink_base_path))

    def arguments(self):
        """
        Parses the arguments and options passed to the script.
        Allows for both long and short forms of 'term' and 'course' when
        running the script.

        :return type: tuple
        :return: args and options
        """

    def run(self):
        return self.question1('fa13', 'cs311')


"""
Question 2

Finds the greatest product of five consecutive digits in the 1000-digit number:

      73167176531330624919225119674426574742355349194934
      96983520312774506326239578318016984801869478851843
      85861560789112949495459501737958331952853208805511
      12540698747158523863050715693290963295227443043557
      66896648950445244523161731856403098711121722383113
      62229893423380308135336276614282806444486645238749
      30358907296290491560440772390713810515859307960866
      70172427121883998797908792274921901699720888093776
      65727333001053367881220235421809751254540594752243
      52584907711670556013604839586446706324415722155397
      53697817977846174064955149290862569321978468622482
      83972241375657056057490261407972968652414535100474
      82166370484403199890008895243450658541227588666881
      16427171479924442928230863465674813919123162824586
      17866458359124566529476545682848912883142607690042
      24219022671055626321111109370544217506941658960408
      07198403850962455444362981230987879927244284909188
      84580156166097919133875499200524063689912560717606
      05886116467109405077541002256983155200055935729725
      71636269561882670428252483600823257530420752963450
"""

"""
Question 3

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

See the posted examples for how to work with a file. For this, A = 1, B = 2,
etc. 
"""

"""
Question 4

The nth term of the sequence of triangle numbers is given by, tn = (1/2)n (n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English
words, how many are triangle words? 
"""

if __name__ == "__main__":
    Main().run()