import 'package:flutter/material.dart';

class RocketInformationWidget extends StatefulWidget {
  const RocketInformationWidget({Key? key}) : super(key: key);

  @override
  _RocketInformationWidgetState createState() =>
      _RocketInformationWidgetState();
}

class _RocketInformationWidgetState extends State<RocketInformationWidget> {
  List<Map<String, dynamic>> _components = [];

  @override
  void initState() {
    _components = [
      {
        'title': 'Nose',
        'id': '123456',
        'active': true,
      },
      {
        'title': 'Cilyndrical body',
        'id': '123fsd456',
        'active': true,
      },
      {
        'title': 'Transition',
        'id': '1sdf23456',
        'active': true,
      },
      {
        'title': 'Cilyndrical body',
        'id': '12345fds6',
        'active': true,
      },
      {
        'title': 'Fins   ',
        'id': '1as234sd56',
        'active': true,
      },
      {
        'title': 'Internal component',
        'id': '1asds23sd4sd56',
        'active': true,
      },
    ];
    super.initState();
  }

  void _changeComponentsStatus(String id) {
    List<Map<String, dynamic>> aux = List.from(_components);
    final int index = aux.indexWhere((element) => element['id'] == id);
    final Map<String, dynamic> map = aux[index];
    map['active'] = !map['active'];
    aux[index] = map;
    setState(() {
      _components = List.from(aux);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: Alignment.topLeft,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Container(
                decoration: BoxDecoration(
                  color: Colors.green,
                  shape: BoxShape.circle,
                ),
                width: 10,
                height: 10,
              ),
              SizedBox(
                width: 10,
              ),
              Text(
                'Rocket components:',
                style: TextStyle(
                  fontSize: 12,
                  color: Colors.grey[700],
                  fontWeight: FontWeight.w500,
                ),
              ),
            ],
          ),
          ..._components
              .map((e) => _item(
                    map: e,
                    onPressed: () => _changeComponentsStatus(e['id']),
                  ))
              .toList(),
        ],
      ),
    );
  }

  Widget _item(
          {required Map<String, dynamic> map,
          required void Function() onPressed}) =>
      Padding(
        padding: const EdgeInsets.only(left: 10),
        child: SizedBox(
          height: 20,
          child: TextButton.icon(
            onPressed: onPressed,
            icon: SizedBox(
              width: 20,
              child: Icon(
                map['active'] ? Icons.visibility : Icons.visibility_off,
                size: 13,
                color: map['active'] ? Colors.grey[500] : Colors.grey[400],
              ),
            ),
            label: Text(
              map['title'],
              style: TextStyle(
                  fontSize: 12,
                  color: map['active'] ? Colors.grey[700] : Colors.grey[500],
                  fontWeight: FontWeight.w300),
            ),
          ),
        ),
      );
}
