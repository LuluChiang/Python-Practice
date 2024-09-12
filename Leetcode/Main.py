# Version: 2021/09/24
#
import LeetcodeProblem

def main():
    print("Practice Start: ")


    # nums_list = [8, 2, 9, 7]
    nums_list = [0,1,2,2,3,0,4,2]
    target = 2


    solution = LeetcodeProblem.Solution()
    opt_list = solution.removeElement(nums_list, target)
    # opt_list = solution.plusOne(nums_list)
    print(opt_list)



if __name__ == '__main__':
        main()
