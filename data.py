
in_data = {
    u'deliveryOrder': {
        u'warehouseCode': u'OTHER',
        u'deliveryOrderCode': u'3600120100000',
        u'receiverInfo': {
            u'detailAddress': u'\u5927\u5382\u680818\u53f7101',
            u'city': u'\u4e94\u8fde',
            u'province': u'\u5c71\u4e1c',
            u'area': u'\u5927\u5382'
        },
        u'senderInfo': {
            u'detailAddress': u'\u6587\u4e09\u8def172\u53f7',
            u'city': u'\u676d\u5dde',
        },
    },
    u'orderLines': {
        u'orderLine': [
            {
                u'itemId': u'0192010101',
                u'planQty': u'20',
            },
            {
                u'itemId': u'0192010102',
                u'planQty': u'30',
            }]
    }
}

mapping = [
    ([u'deliveryOrder', u'warehouseCode'], 'warehouse_code'),
    ([u'deliveryOrder', u'deliveryOrderCode'], 'express_code'),

    ([u'deliveryOrder', u'receiverInfo', u'area'], 'receiver_area'),
    ([u'deliveryOrder', u'receiverInfo', u'province'], 'receiver_province'),
    ([u'deliveryOrder', u'receiverInfo', u'detailAddress'], 'receiver_address'),
    ([u'deliveryOrder', u'receiverInfo', u'city'], 'receiver_city'),

    ([u'deliveryOrder', u'senderInfo', u'city'], 'sender_city'),
    ([u'deliveryOrder', u'senderInfo', u'detailAddress'], 'sender_address'),

    ([u'orderLines', u'orderLine'], 'lines', [
        ([u'itemId'], 'item_id'),
        ([u'planQty'], 'product_qty'),
    ])

]
