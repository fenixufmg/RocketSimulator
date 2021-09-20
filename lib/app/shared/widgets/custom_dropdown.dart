import 'package:flutter/material.dart';

class CustomDropdown extends StatefulWidget {
  final void Function(String value) onChanged;
  final List<String> items;
  final String title;
  const CustomDropdown({Key? key,
    required this.onChanged,
    required this.items,
    required this.title,
  }) : super(key: key);

  @override
  _CustomDropdownState createState() => _CustomDropdownState();
}

class _CustomDropdownState extends State<CustomDropdown> {

  String? _material;

  void _changeMaterial(String value) {
    setState(() {
      _material = value;
    });
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: DropdownButton<String>(
        hint: Text(
          widget.title,
        ),
        value: _material,
        isExpanded: true,
        items: widget.items.map((String value) {
          return DropdownMenuItem<String>(
            value: value,
            child: Text(
              '${widget.title}: $value'
            ),
          );
        }).toList(),
        onChanged: (String? value) {
          _changeMaterial(value!);
          widget.onChanged(value);
        },
      ),
    );
  }
}