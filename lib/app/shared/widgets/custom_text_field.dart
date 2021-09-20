import 'package:flutter/material.dart';
import 'package:rocket_simulator/app/shared/theme/app_colors.dart';

class CustomTextField extends StatelessWidget {
  final void Function(String? value) onSaved;
  final String? Function(String? value) validator;
  final String label;
  final String? initialValue;
  const CustomTextField({
    Key? key,
    required this.onSaved,
    required this.validator,
    required this.label,
    this.initialValue,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      onSaved: onSaved,
      validator: validator,
      initialValue: initialValue,
      decoration: InputDecoration(
        labelText: label,
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(5.0),
          borderSide: BorderSide(
            color: AppColors.red,
          ),
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(5.0),
          borderSide: BorderSide(
            color: Colors.grey[300]!,
            width: 2.0,
          ),
        ),
      ),
    );
  }
}
