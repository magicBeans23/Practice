class CurlAnalytics:
    @staticmethod
    def candies(k, b, candy_counts):
        assert len(candy_counts) == k
        n = sum(candy_counts)
        if n % b == 0:
            return n//b
        else:
            return 0
    @staticmethod
    def getdate(text):
        from dateutil.parser import parse
        try:
            p = parse(text.replace('.', ''), fuzzy=True)
            return p.strftime("%B, %d %Y")
        except ValueError:
            return None




if __name__ == '__main__':
    print(CurlAnalytics.candies(5, 3, [1, 2, 3, 4, 5]))
    print(CurlAnalytics.candies(5, 8, [1, 2, 3, 4, 5]))
    print(CurlAnalytics.getdate('Central design committee session Tuesday 10/22 6:30 pm'))
    print(CurlAnalytics.getdate('Lorem ipsum. Lorem ipsum'))