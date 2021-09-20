import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:view/view.dart';

import '../../../../../shared/widgets/custom_dropdown.dart';
import '../../../../../shared/widgets/custom_text_field.dart';
import '../../../../../shared/widgets/general_dialog.dart';

class FinInput extends StatelessWidget {
  const FinInput({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GeneralDialog(
      title: 'Fins',
      alertMessage: 'Your rocket must start with a Nose',
      content: SingleChildScrollView(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            CustomTextField(
              label: 'Root chord [mm]',
              onSaved: (String? value) {},
              validator: (String? value) {},
            ),
            SizedBox(
              height: 7,
            ),
            CustomTextField(
              label: 'Tip chord [mm]',
              onSaved: (String? value) {},
              validator: (String? value) {},
            ),
            SizedBox(
              height: 7,
            ),
            CustomTextField(
              label: 'Span [mm]',
              onSaved: (String? value) {},
              validator: (String? value) {},
            ),
            SizedBox(
              height: 7,
            ),
            CustomTextField(
              label: 'Swept angle [degrees]',
              onSaved: (String? value) {},
              validator: (String? value) {},
            ),
            SizedBox(
              height: 7,
            ),
            CustomTextField(
              label: 'Number of fins',
              onSaved: (String? value) {},
              validator: (String? value) {},
            ),
            SizedBox(
              height: 7,
            ),
            CustomTextField(
              label: 'Max. Thickness',
              onSaved: (String? value) {},
              validator: (String? value) {},
            ),
            SizedBox(
              height: 7,
            ),
            CustomTextField(
              label: 'Surface Roughness [mm]',
              onSaved: (String? value) {},
              validator: (String? value) {},
            ),
            SizedBox(
              height: 10,
            ),
            Padding(
              padding: const EdgeInsets.symmetric(
                horizontal: 3.5,
              ),
              child: CustomDropdown(
                onChanged: (String? value) {},
                items: modelMaterials.map<String>((e) => e['name']).toList(),
                title: 'Material',
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
