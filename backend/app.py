@app.route('/api/notes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_notes():
    if request.method == 'GET':
        return jsonify(notes)
    elif request.method == 'POST':
        data = request.get_json()
        new_note = {'text': data['text'], 'id': len(notes) + 1}
        notes.append(new_note)
        return jsonify(new_note), 201
    elif request.method == 'PUT':
        data = request.get_json()
        note_id = int(data['id'])
        updated_text = data['text']
        for note in notes:
            if note['id'] == note_id:
                note['text'] = updated_text
                return jsonify(note), 200
        return '', 404 
    elif request.method == 'DELETE':
        note_id = int(request.args.get('id'))
        notes[:] = [note for note in notes if note['id'] != note_id]
        return '', 204
