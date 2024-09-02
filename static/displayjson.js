function renderJsonData(data, container, isNested = false) {
    Object.keys(data).forEach(key => {
        const value = data[key];
        // Determine if we should use a table layout (vertical) or card layout (horizontal)
        const useTableLayout = typeof value === 'object' && !Array.isArray(value) && value !== null;

        // Create a container element (card or table)
        const card = document.createElement('div');
        card.className = isNested ? 'json-card nested' : useTableLayout ? 'json-table' : 'json-card';

        // Create subtitle for each key
        const subtitle = document.createElement('h5');
        subtitle.className = 'text-primary';
        subtitle.textContent = key.charAt(0).toUpperCase() + key.slice(1);
        card.appendChild(subtitle);

        if (useTableLayout) {
            // Render as a table for nested objects
            const table = document.createElement('table');
            table.className = 'table table-bordered';

            Object.keys(value).forEach(subKey => {
                const row = document.createElement('tr');

                const cellKey = document.createElement('th');
                cellKey.textContent = subKey.charAt(0).toUpperCase() + subKey.slice(1);
                row.appendChild(cellKey);

                const cellValue = document.createElement('td');
                const subValue = value[subKey];
                cellValue.textContent = typeof subValue === 'object' ? JSON.stringify(subValue) : subValue;
                row.appendChild(cellValue);

                table.appendChild(row);
            });

            card.appendChild(table);
        } else if (Array.isArray(value) && value.length > 0) {
            // Render array items as list inside a card
            const list = document.createElement('ul');
            list.className = 'list-group list-group-flush';

            value.forEach(item => {
                const listItem = document.createElement('li');
                listItem.className = 'list-group-item';
                listItem.textContent = item;
                list.appendChild(listItem);
            });

            card.appendChild(list);
        } else if (value !== null && value !== undefined) {
            // Render other types directly inside a card
            const list = document.createElement('ul');
            list.className = 'list-group list-group-flush';

            const listItem = document.createElement('li');
            listItem.className = 'list-group-item';
            listItem.textContent = value;

            list.appendChild(listItem);
            card.appendChild(list);
        } else {
            // Handle empty objects, arrays, or null values
            const emptyNotice = document.createElement('p');
            emptyNotice.className = 'text-muted';
            emptyNotice.textContent = '(empty)';
            card.appendChild(emptyNotice);
        }

        container.appendChild(card);
    });
}



function renderJsonData2(data, container, isNested = false) {
    Object.keys(data).forEach(key => {
        const value = data[key];
        // Determine if we should use a table layout (vertical) or card layout (horizontal)
        const useTableLayout = typeof value === 'object' && !Array.isArray(value) && value !== null;

        // Create a container element (card or table)
        const card = document.createElement('div');
        card.className = isNested ? 'json-card nested col-md-12' : useTableLayout ? 'json-table col-md-6' : 'json-card col-md-4';

        // Create subtitle for each key
        const subtitle = document.createElement('h5');
        subtitle.className = 'text-primary';
        subtitle.textContent = key.charAt(0).toUpperCase() + key.slice(1);
        card.appendChild(subtitle);

        if (useTableLayout) {
            // Render as a table for nested objects
            const table = document.createElement('table');
            table.className = 'table table-bordered';

            Object.keys(value).forEach(subKey => {
                const row = document.createElement('tr');

                const cellKey = document.createElement('th');
                cellKey.textContent = subKey.charAt(0).toUpperCase() + subKey.slice(1);
                row.appendChild(cellKey);

                const cellValue = document.createElement('td');
                const subValue = value[subKey];
                cellValue.textContent = typeof subValue === 'object' ? JSON.stringify(subValue) : subValue;
                row.appendChild(cellValue);

                table.appendChild(row);
            });

            card.appendChild(table);
        } else if (Array.isArray(value) && value.length > 0) {
            // Render array items as list inside a card
            const list = document.createElement('ul');
            list.className = 'list-group list-group-flush';

            value.forEach(item => {
                const listItem = document.createElement('li');
                listItem.className = 'list-group-item';
                listItem.textContent = item;
                list.appendChild(listItem);
            });

            card.appendChild(list);
        } else if (value !== null && value !== undefined) {
            // Render other types directly inside a card
            const list = document.createElement('ul');
            list.className = 'list-group list-group-flush';

            const listItem = document.createElement('li');
            listItem.className = 'list-group-item';
            listItem.textContent = value;

            list.appendChild(listItem);
            card.appendChild(list);
        } else {
            // Handle empty objects, arrays, or null values
            const emptyNotice = document.createElement('p');
            emptyNotice.className = 'text-muted';
            emptyNotice.textContent = '(empty)';
            card.appendChild(emptyNotice);
        }

        container.appendChild(card);
    });
}
