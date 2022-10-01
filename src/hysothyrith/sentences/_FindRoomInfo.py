def sentences():
    return [
        # * Simple
        ["បន្ទ់ប១០១នៅទីណា?", ["Room:101"]],
        ["បន្ទប់៣០១នៅជាន់ទីប៉ុន្មាន?", ["Room:301", "Floor"]],
        # * With associations
        ["បន្ទប់៣០១គេកំពុងរៀនអ្វីនឹង?", ["Room:301", "Subject"]],
        ["បន្ទប់១២៣គេកំពុងមានកម្មវិធីអ្វី?", ["Room:123", "Event"]],
        ["បន្ទប់លោកគ្រូសុផានៅឯណា?", ["Room", "Lecturer:sopha"]],
        [
            "បន្ទប់រៀនជាមួយគ្រូសុខានៅម្តុំណា?",
            ["Room", "Lecturer:sokha", "Activity:study"],
        ],
        ["ឯណាទៅបន្ទប់សិក្សាម៉ោងProgramming?", ["Room", "Subject:programming"]],
        ["ឯណាទៅបន្ទប់សិក្សាថ្នាក់Programming?", ["Room", "Subject:programming"]],
        [
            "បន្ទប់ប្រលងDiscrete mathនៅណាបង?",
            ["Room", "Exam", "Subject:discrete_math", "Me"],
        ],
        [
            "បន្ទប់១២៣គេកំពុងមានកម្មវិធីអ្វីនៅថ្ងៃនេះ?",
            ["Room:123", "Event", "Time:today"],
        ],
        [
            "បន្ទប់នៅជាប់បន្ទប់ទឹកជាន់ទី១គេសម្រាប់ធ្វើអ្វី?",
            ["Room", "Toilet", "Floor:1", "RoomPurpose"],
        ],
        # * Ambiguous
        ["តើបន្ទប់Justinនៅឯណា?", ["Room:justin", "Person:justin"]],
    ]
