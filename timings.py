
class Timings:
    def __init__(self, start_minute, start_second, end_minute, end_second):
        self.start_minute = start_minute
        self.start_second = start_second
        self.end_minute = end_minute
        self.end_second = end_second


voice_timings = {
    "1": [
        Timings(30, 20, 32, 3),
        Timings(36, 18, 38, 9),
    ],
    "2": [
        Timings(15, 55, 17, 55),
    ],
    "3": [
        Timings(7, 55, 9, 43),
        Timings(42, 16, 43, 45),
    ],
    "4":[
        Timings(19, 17, 21, 6),
        Timings(33, 3, 34, 18),
    ],
    "5":[
        Timings(12, 6, 13, 48),
        Timings(40, 2, 41, 37),
    ],
    "6":[
        Timings(40, 54, 42, 35),
    ],
    "7":[
        Timings(12, 29, 14, 20),
    ],
    "8":[
        Timings(14, 26, 16, 32),
    ],
    "9":[
        Timings(27, 42, 29, 21),
    ],
    "10":[
        Timings(15, 47, 17, 31),
        Timings(23, 16, 25, 48),
    ],
    "11": [
        Timings(1, 4, 2, 43),
    ],
    "13":[
        Timings(14, 52, 16, 0),
    ],
    "14":[
        Timings(6, 19, 8, 22),
        Timings(36,19, 38, 8)
    ],
    "27" : [
        Timings(30, 20, 32, 3),
        Timings(36, 18, 38, 9),
    ],
    "31": [
        Timings(6, 42, 8, 31),
    ],
    "40": [
        Timings(16, 21, 22, 11),
    ],
    "64": [
        Timings(19, 20, 22, 0),
    ], 
    "65": [
        Timings(13, 26, 17, 6),
    ],
    "67": [
        Timings(14, 43, 17, 58),
    ],
    "74": [
        Timings(6, 27, 9, 1),
    ],
    "79" : [
        Timings(1, 53, 2, 24),
    ],
    "83": [
        Timings(15, 51, 17, 4),
    ],
    "85": [
        Timings(5, 10, 7, 50),
    ],
    "108": [
        Timings(18, 54, 22, 27),
    ],
    "116": [
        Timings(7, 47, 8, 51),
    ],
    "118":[
        Timings(1,48,3,0),
        Timings(4, 25, 5, 50),
    ],
    "131":[
        Timings(4, 45, 8, 53),
    ],
    "134":[
        Timings(15, 44, 18, 1),
    ],
    "155": [
        Timings(4, 17, 6, 2),
        Timings(7, 10, 8, 25),
    ],
    "158": [
        Timings(5, 47, 7, 16),
        Timings(17,21,20,44)
    ],
    "162":[
        Timings(0, 55, 2, 5),
    ],
    "190":[
        Timings(23,39,25,20),
        Timings(26,13,27,45),
        Timings(33,1,33,20),
    ],
    "197": [
        Timings(35, 12, 37, 28),
    ],
    "198": [
        Timings(38, 53, 43, 40),
    ],

}

subclip_timings = {
    "1subclip": [
        Timings(0, 0, 2, 35),
    ],
}
#160
#164