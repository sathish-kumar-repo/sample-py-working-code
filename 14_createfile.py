import os

os.chdir("D:\\Flutter Project\\learn_smart\\lib\\learn\\JayCutlerTv\\jayCutlerEnglish")
for i in range(1, 901):
    f = open(f"{i}_jayCutlerVideo.dart", "w")
    f.write(
        """
import 'package:flutter/material.dart';
import 'package:learn_smart/CustomWidgets/customBody.dart';
import 'package:learn_smart/CustomWidgets/standardWidget.dart';

class Title extends StatelessWidget {
  const Title({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const customBody(
      childrens: [
        h1(text: 'title'),
        CP(txt: ''),
      ],
    );
  }
}

"""
    )
