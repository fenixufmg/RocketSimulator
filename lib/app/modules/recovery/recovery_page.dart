import 'package:flutter/material.dart';
import 'package:rocket_simulator/app/shared/theme/app_colors.dart';

class RecoveryPage extends StatelessWidget {
  const RecoveryPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Text('Recovery');

    // return Expanded(
    //   child: Stack(
    //     children: [

    //       Align(
    //         child: IconButton(
    //           icon: Icon(
    //             Icons.save,
    //             color: AppColors.white,
    //           ),
    //           onPressed: () {},
    //           color: AppColors.blueLight,
    //         ),
    //       )
    //     ],
    //   ),
    // );
  }
}