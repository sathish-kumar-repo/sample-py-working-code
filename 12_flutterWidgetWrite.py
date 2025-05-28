import os

os.chdir("D:\\Flutter Project\\learn_smart\\lib\\learn\\Course6_Flutter_Widget\\")
my_list = os.listdir("widgetsTutorialLive")


def extract_class_name(file_name):
    # Remove file extension
    class_name = file_name.split(".")[0]

    # Remove preceding characters (e.g., 'Widgets1_', 'Widgets2_')
    class_name = class_name.split("_")[-1]

    return class_name


def extract_number(s):
    return int("".join(filter(str.isdigit, s)))


# Sort the list using the custom sorting function
sorted_list = sorted(my_list, key=extract_number)
# print(sorted_list)
widgetName = [extract_class_name(file_name) for file_name in sorted_list]

for j, i in enumerate(sorted_list):
    print(
        f"Search('{widgetName[j]} Widget', const Flutter{widgetName[j]}FlutterAllWidgets()),"
    )
    # print(
    #     f"import 'package:learn_smart/learn/Course6_Flutter_Widget/fw{j+1}_{widgetName[j]}.dart';"
    # )

# # testlist = list(sorted_list[0:3])
# # print(testlist)

#


# for j, i in enumerate(sorted_list):
#     f = open(f"widgetsTutorialLive\\{i}", "r", encoding="utf8")
#     data = f.readlines()
#     # temp = []
#     # for x in data:
#     #     new = x.replace("\n", "")
#     #     temp.append(new)
#     listToStr = " ".join([str(elem) for elem in data])

#     txt = (
#         """
# import 'package:flutter/material.dart';
# import 'package:learn_smart/CustomWidgets/CustomCodeHighlighter.dart';
# import 'package:learn_smart/CustomWidgets/customBody.dart';
# import 'package:learn_smart/CustomWidgets/customDrawer.dart';
# import 'package:learn_smart/CustomWidgets/standardWidget.dart';
# import 'package:learn_smart/components/appBar.dart';
# import 'package:learn_smart/learn/Course6_Flutter_Widget/TopicName/widgetTopic.dart';
# import 'package:learn_smart/learn/Course6_Flutter_Widget/widgetsTutorialLive/"""
#         + str(i)
#         + """';

# class """
#         + """Flutter"""
#         + widgetName[j]
#         + """FlutterAllWidgets"""
#         + """ extends StatefulWidget {
#   const """
#         + """Flutter"""
#         + widgetName[j]
#         + """FlutterAllWidgets"""
#         + """({Key? key}) : super(key: key);

#   @override
#   State<"""
#         + """Flutter"""
#         + widgetName[j]
#         + """FlutterAllWidgets"""
#         + """> createState() => _"""
#         + """Flutter"""
#         + widgetName[j]
#         + """FlutterAllWidgets"""
#         + """State();
# }

# class _"""
#         + """Flutter"""
#         + widgetName[j]
#         + """FlutterAllWidgets"""
#         + """State extends State<"""
#         + """Flutter"""
#         + widgetName[j]
#         + """FlutterAllWidgets"""
#         + """> {
#   @override
#   Widget build(BuildContext context) {
#     return Scaffold(
#       appBar: const CustomAppBar(),
#       drawer: CustomDrawer(
#         activeIndex: """
#         + str(j + 1)
#         + """,
#         topicsName: WidgetsTopics,
#         img: 'Flutter.png',
#         contain: true,
#       ),
#       body: customBody(
#         childrens: [
#           const h1(text: '"""
#         + str(widgetName[j])
#         + """ Widget'),
#           const h3(text: 'Click to View Live'),
#           const Live(page: """
#         + str(widgetName[j])
#         + """Widget()),
#           const h3(text: 'Source Code'),
#           Code(title: 'main.dart', code: code, type: 'dart'),
#         ],
#       ),
#     );
#   }
# }

# var code = '''
# """
#         + listToStr
#         + """
# ''';
# """
#     )
#     with open(f"fw{j+1}_{widgetName[j]}.dart", "w", encoding="utf-8") as f:
#         f.write(txt)
