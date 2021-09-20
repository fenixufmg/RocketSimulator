import 'package:flutter/material.dart';
import 'package:rocket_simulator/app/shared/theme/app_colors.dart';

class ItemsWidget extends StatefulWidget {
  final List<ColumnItem> items;
  const ItemsWidget({
    Key? key,
    required this.items,
  }) : super(key: key);

  @override
  _ItemsWidgetState createState() => _ItemsWidgetState();
}

class _ItemsWidgetState extends State<ItemsWidget> {
  late List<ColumnItem> _items;

  @override
  void initState() {
    _items = widget.items;
    super.initState();
  }

  void _changeItemStatus(String title) {
    final _index = widget.items.indexWhere((element) => element.title == title);
    if (!_items[_index].active) {
      List<ColumnItem> _aux = _items
          .map((e) => ColumnItem(
                title: e.title,
                active: e.title == title,
                onPressed: e.onPressed,
                icon: e.icon,
              ))
          .toList();
      setState(() {
        _items = List.from(_aux);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
        width: MediaQuery.of(context).size.width,
        color: AppColors.red,
        padding: EdgeInsets.symmetric(horizontal: 5),
        child: Row(
          children: _items
              .map(
                (e) => _item(
                  onPressed: () {
                    print(e.title);
                    _changeItemStatus(e.title);
                    e.onPressed();
                  },
                  title: e.title,
                  active: e.active,
                  icon: e.icon,
                ),
              )
              .toList(),
        ));
  }

  Widget _item(
          {required void Function() onPressed,
          required String title,
          required bool active,
          required String icon}) =>
      Container(
        width: 80,
        height: 80,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Spacer(),
            MaterialButton(
              minWidth: 80,
              onPressed: onPressed,
              child: Column(
                children: [
                  Image(
                    image: AssetImage('assets/' + icon),
                    color: active ? AppColors.white : AppColors.white.withOpacity(0.5),
                    height: 30,
                  ),
                  SizedBox(
                    height: 5,
                  ),
                  Text(
                    title,
                    style: TextStyle(
                      color: active ? AppColors.white : AppColors.white.withOpacity(0.5),
                      fontWeight: FontWeight.w300,
                      fontSize: 11,
                    ),
                  ),
                ],
              ),
            ),
            Spacer(),
            Container(
              decoration: BoxDecoration(
                  color: active ? AppColors.white : Colors.transparent,
                  borderRadius: BorderRadius.only(
                    topLeft: Radius.circular(5),
                    topRight: Radius.circular(5),
                  )),
              height: 3,
              width: 50,
            )
          ],
        ),
      );
}

class ColumnItem {
  final String title;
  final bool active;
  final void Function() onPressed;
  final String icon;
  ColumnItem(
      {required this.title, required this.active, required this.onPressed, required this.icon});

  ColumnItem get changeActive => ColumnItem(
        title: this.title,
        active: !this.active,
        onPressed: this.onPressed,
        icon: this.icon,
      );
}
