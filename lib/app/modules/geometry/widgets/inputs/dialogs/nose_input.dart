import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:view/view.dart';

import '../../../../../shared/widgets/custom_dropdown.dart';
import '../../../../../shared/widgets/custom_text_field.dart';
import '../../../../../shared/widgets/general_dialog.dart';

class NoseInput extends StatelessWidget {
  const NoseInput({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GeneralDialog(
        title: 'Nose',
        content: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              CustomTextField(
                label: 'Diameter [mm]',
                onSaved: (String? value) {},
                validator: (String? value) {},
              ),
              SizedBox(
                height: 7,
              ),
              CustomTextField(
                label: 'Height [mm]',
                onSaved: (String? value) {},
                validator: (String? value) {},
              ),
              SizedBox(
                height: 7,
              ),
              CustomTextField(
                label: 'Thickness [mm]',
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
                  items: noseShapes.map<String>((e) => e['name']).toList(),
                  title: 'Geometry',
                ),
              ),
              SizedBox(
                height: 7,
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