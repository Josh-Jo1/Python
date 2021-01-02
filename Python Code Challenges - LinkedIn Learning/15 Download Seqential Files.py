# Challenge: Write a Python function to download and save a sequence of files.
# Input: URL for first item, output directory path
# Provided example: http://699340.youcanlearnit.net/image001.jpg to http://699340.youcanlearnit.net/image050.jpg

# Assume last 3 characters before extension are always numbers for sequence
# Assume last 4 characters are always extension


import requests

def downloadFiles(firstURL, outputPath):
    # Split up firstURL
    url = firstURL[:-7]
    counter = int(firstURL[-7:-4])
    ext = firstURL[-4:]

    while True:
        currentURL = url + f"{counter:03d}" + ext       # url + 001 + ext   to   url + 050 + ext
        response = requests.get(currentURL, allow_redirects=True)

        if response:
            with open(outputPath + "\\file" + f"{counter:03d}" + ext, 'wb') as file:
                file.write(response.content)
        else:
            break

        counter += 1


firstItem = input()
path = input()
# firstItem = "http://699340.youcanlearnit.net/image001.jpg"
# path = "C:\\Users\\User\\Desktop\\Files"

downloadFiles(firstItem, path)







#                     *  *  *
#                  *           *
#                 *    *   *    *
#                 *      *      *
#         *       *   *     *   *       *
#          *       *   * * *   *       *
#       *   *       *         *       *   *
#         *  *        *  *  *        *  *
#             *    *           *    *
#               * *             * *
#                 *             *
#                  *           *
#                     *  *  *
#                  *           *
#                 *             *
#                 *             *
#                  *           *
#                     *  *  *
