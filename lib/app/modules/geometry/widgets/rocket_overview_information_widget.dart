import 'package:flutter/material.dart';

class RocketOverviewInformationWidget extends StatelessWidget {
  const RocketOverviewInformationWidget({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: Alignment.bottomCenter,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            'Mass:  -  kg',
            style: TextStyle(
              color: Colors.grey[700]
            ),
          ),
          SizedBox(width: 30,),
          Text(
            'Cp:  -',
            style: TextStyle(
              color: Colors.grey[700]
            ),
          ),
          SizedBox(width: 30,),
          Text(
            'CG:  -',
            style: TextStyle(
              color: Colors.grey[700]
            ),
          ),
        ],
      ),
    );
  }
}