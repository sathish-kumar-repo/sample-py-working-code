lst = [
    "Course Overview",
    "Dart Setup",
    "Hello World",
    "Comments",
    "Variables And Datatypes",
    "String Interpolation",
    "Dart Constants",
    "Conditional Statement",
    "Conditional Expression",
    "Looping Statement",
    "Functions",
    "Exception Handling",
    "Class And Object",
    "Constructors",
    "Object Oriented Dart",
    "Getter And Setter",
    "Inheritance",
    "Method Overiding",
    "Constructor During Inheritance",
    "Abstract Class",
    "Interface",
    "Static keyword",
    "Lambda",
    "Higher Order Function",
    "Lexical Closures",
    "List",
    "Set And HashSet",
    "Map And HashMap",
    "Callable Classes",
]
for i in lst:
    c = i.replace(" ", "")
    print(f"Topics('{i}', const Dart{c}(), 'dart'),")
# import os

# os.chdir("D:\\Flutter Project\\learn_smart\\lib\\learn\\Course8_DartCore")


# for j, i in enumerate(lst):
#     k = i.replace(" ", "_")
#     c = i.replace(" ", "")
#     f = open(f"dart_core{j}_{k}.dart", "w")
#     f.write(
#         """
# import 'package:flutter/material.dart';
# import 'package:learn_smart/CustomWidgets/CustomCodeHighlighter.dart';
# import 'package:learn_smart/CustomWidgets/customBody.dart';
# import 'package:learn_smart/CustomWidgets/customDrawer.dart';
# import 'package:learn_smart/CustomWidgets/standardWidget.dart';
# import 'package:learn_smart/components/appBar.dart';
# import 'package:learn_smart/learn/Course8_DartCore/topicsName/dartCoreTopics.dart';

# class """
#         + """Dart"""
#         + c
#         + """ extends StatefulWidget {
#   const """
#         + """Dart"""
#         + c
#         + """({Key? key}) : super(key: key);

#   @override
#   State<"""
#         + """Dart"""
#         + c
#         + """> createState() => _"""
#         + """Dart"""
#         + c
#         + """State();
# }

# class _"""
#         + """Dart"""
#         + c
#         + """State extends State<"""
#         + """Dart"""
#         + c
#         + """> {
#   @override
#   Widget build(BuildContext context) {
#     return Scaffold(
#       appBar: const CustomAppBar(),
#       drawer: CustomDrawer(
#         activeIndex: """
#         + str(j + 1)
#         + """,
#         topicsName: dartCoreTopics,
#         img: 'dart.png',
#         contain: true,
#       ),
#       body: customBody(
#         childrens: [
#           const h1(text: '"""
#         + i
#         + """'),
#         ],
#       ),
#     );
#   }
# }
# """
#     )
