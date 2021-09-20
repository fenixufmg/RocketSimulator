import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';

import '../../../../../shared/widgets/custom_dropdown.dart';
import '../../../../../shared/widgets/custom_text_field.dart';
import '../../../../../shared/widgets/general_dialog.dart';

class InternalComponentInput extends StatelessWidget {
  const InternalComponentInput({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GeneralDialog(
      title: 'Internal Component',
      alertMessage: 'Your rocket must start with a Nose',
      content: SingleChildScrollView(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            CustomTextField(
              label: 'Size [mm]',
              onSaved: (String? value) {},
              validator: (String? value) {},
            ),
            SizedBox(
              height: 5,
            ),
            CustomTextField(
              label: 'Position from tip [mm]',
              onSaved: (String? value) {},
              validator: (String? value) {},
            ),
            SizedBox(
              height: 5,
            ),
            CustomTextField(
              label: 'Mass [kg]',
              onSaved: (String? value) {},
              validator: (String? value) {},
            ),
            Padding(
              padding: const EdgeInsets.symmetric(
                horizontal: 3.5,
              ),
              child: CustomDropdown(
                onChanged: (String? value) {},
                items: ['A', 'B', 'C', 'D'],
                title: 'Geometry',
              ),
            ),
          ],
        ),
      ),
      accept: () {},
      cancel: () => Modular.to.pop(),
    );
  }
}
