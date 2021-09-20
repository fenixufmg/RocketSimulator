import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:rocket_simulator/app/shared/theme/app_colors.dart';

import 'custom_button.dart';

class GeneralDialog extends StatelessWidget {
  final String title;
  final String? alertMessage;
  final Widget content;
  final void Function()? accept;
  final void Function()? cancel;
  const GeneralDialog(
      {Key? key,
      required this.title,
      required this.content,
      this.alertMessage,
      this.accept,
      this.cancel})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            title,
          ),
          IconButton(
            onPressed: () => Modular.to.pop(),
            icon: Icon(
              Icons.close,
            ),
          ),
        ],
      ),
      content: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          ...alertMessage != null
              ? [
                  Container(
                    height: 40,
                    width: double.infinity,
                    color: AppColors.red.withOpacity(0.5),
                    padding: EdgeInsets.symmetric(
                      horizontal: 10,
                    ),
                    child: Align(
                      alignment: Alignment.centerLeft,
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            Icons.error_outline,
                            color: Colors.red[700],
                          ),
                          SizedBox(width: 5,),
                          Text(
                            alertMessage!,
                            style: TextStyle(
                              color: Colors.red[700],
                            ),
                          )
                        ],
                      ),
                    ),
                  ),
                  SizedBox(
                    height: 10,
                  ),
                ]
              : [
                  SizedBox(
                    width: 0.0,
                    height: 0.0,
                  )
                ],
          content,
        ],
      ),
      actions: [
        cancel != null
            ? CustomButton(
                color: Colors.grey[300]!,
                labelColor: Colors.grey[700]!,
                label: 'Cancel',
                onPressed: () => Modular.to.pop(),
              )
            : SizedBox(
                height: 0.0,
                width: 0.0,
              ),
        accept != null
            ? CustomButton(
                color: AppColors.red,
                labelColor: AppColors.white,
                label: 'Accept',
                onPressed: () {},
              )
            : SizedBox(
                height: 0.0,
                width: 0.0,
              ),
      ],
    );
  }
}
