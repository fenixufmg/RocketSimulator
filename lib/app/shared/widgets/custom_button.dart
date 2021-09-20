import 'package:flutter/material.dart';

class CustomButton extends StatelessWidget {
  final Color color;
  final Color labelColor;
  final String label;
  final void Function() onPressed;
  const CustomButton({Key? key,
    required this.color,
    required this.labelColor,
    required this.label,
    required this.onPressed,}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextButton(
      child: SizedBox(
        width: 100,
        height: 30,
        child: Center(
          child: Text(
            label,
          ),
        ),
      ),
      style: TextButton.styleFrom(
        primary: labelColor,
        backgroundColor: color,
        onSurface: Colors.grey,
      ),
      onPressed: onPressed,
    );
  }
}
