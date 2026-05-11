// ===============================
// ADVANCED 3D DASHBOARD GRAPHS
// REPLACE FULL dashboard.js
// ===============================

// ===============================
// 3D PIE CHART
// ===============================

function updatePieChart(completed, pending) {

Plotly.newPlot('dashboardPie', [

{
    labels: ['Completed', 'Pending'],

    values: [completed, pending],

    type: 'pie',

    hole: 0.45,

    textinfo: 'label+percent+value',

    textfont: {
        size: 18,
        color: 'white'
    },

    marker: {
        colors: [
            '#22c55e',
            '#ef4444'
        ]
    },

    pull: [0.05, 0.03]
}

],

{
    title: {
        text: '🔥 3D Task Completion Analytics',
        font: {
            size: 28,
            color: 'white'
        }
    },

    paper_bgcolor: '#1e293b',

    plot_bgcolor: '#1e293b',

    font: {
        color: 'white'
    },

    height: 650
},

{
    displayModeBar: false
});

}

updatePieChart(5,2);


// ===============================
// 3D BAR GRAPH
// REALISTIC PROFESSIONAL GRAPH
// ===============================

Plotly.newPlot('dashboardBar',

[

{
    x: [

        'Backend',
        'Frontend',
        'Database',
        'Testing',
        'Deployment'

    ],

    y: [

        95,
        88,
        92,
        75,
        90

    ],

    type: 'bar',

    text: [

        '95%',
        '88%',
        '92%',
        '75%',
        '90%'

    ],

    textposition: 'outside',

    marker: {

        color: [

            '#38bdf8',
            '#f43f5e',
            '#22c55e',
            '#facc15',
            '#8b5cf6'

        ],

        line: {
            width: 2,
            color: 'white'
        }
    }
}

],

{
    title: {

        text: '🚀 AI Team Productivity Performance',

        font: {
            size: 28,
            color: 'white'
        }
    },

    paper_bgcolor: '#1e293b',

    plot_bgcolor: '#1e293b',

    font: {
        color: 'white'
    },

    xaxis: {
        title: 'Departments'
    },

    yaxis: {
        title: 'Performance %'
    },

    height: 650
},

{
    displayModeBar: false
});


// ===============================
// 3D WORKFLOW GRAPH
// ===============================

Plotly.newPlot('workflowGraph',

[

{
    type: 'scatter3d',

    mode: 'lines+markers+text',

    x: [1,2,3,4,5,6],

    y: [10,20,35,50,70,95],

    z: [5,10,15,20,30,40],

    text: [

        'Planning',
        'Design',
        'Development',
        'Testing',
        'Deployment',
        'Success'

    ],

    textposition: 'top center',

    marker: {

        size: 8,

        color: [

            '#38bdf8',
            '#f43f5e',
            '#22c55e',
            '#facc15',
            '#8b5cf6',
            '#06b6d4'

        ]
    },

    line: {

        width: 10,

        color: '#38bdf8'
    }
}

],

{
    title: {

        text: '⚡ 3D AI Work Process Flow',

        font: {
            size: 28,
            color: 'white'
        }
    },

    paper_bgcolor: '#1e293b',

    font: {
        color: 'white'
    },

    scene: {

        xaxis: {
            title: 'Workflow Stage'
        },

        yaxis: {
            title: 'Progress'
        },

        zaxis: {
            title: 'AI Accuracy'
        }
    },

    height: 700
},

{
    displayModeBar: false
});


// ===============================
// 3D PERFORMANCE SURFACE GRAPH
// ===============================

let zData = [

[10,20,30,40,50],
[20,35,45,55,65],
[35,50,60,75,85],
[50,65,80,90,100],
[60,75,90,100,110]

];

Plotly.newPlot('surfaceGraph',

[

{
    z: zData,

    type: 'surface',

    colorscale: 'Viridis'
}

],

{
    title: {

        text: '📈 AI Performance Surface Analysis',

        font: {
            size: 28,
            color: 'white'
        }
    },

    paper_bgcolor: '#1e293b',

    font: {
        color: 'white'
    },

    scene: {

        xaxis: {
            title: 'Task Complexity'
        },

        yaxis: {
            title: 'Processing'
        },

        zaxis: {
            title: 'AI Performance'
        }
    },

    height: 700
},

{
    displayModeBar: false
});


// ===============================
// 3D LINE GRAPH
// ===============================

Plotly.newPlot('dashboardLine',

[

{
    type: 'scatter3d',

    mode: 'lines+markers+text',

    x: [1,2,3,4,5,6,7,8,9,10],

    y: [10,20,30,45,60,72,80,88,95,100],

    z: [5,10,12,18,22,30,35,40,45,50],

    text: [

        '10%',
        '20%',
        '30%',
        '45%',
        '60%',
        '72%',
        '80%',
        '88%',
        '95%',
        '100%'

    ],

    textposition: 'top center',

    marker: {

        size: 7,

        color: '#38bdf8'
    },

    line: {

        width: 8,

        color: '#38bdf8'
    }
}

],

{
    title: {

        text: '📊 3D Productivity Growth',

        font: {
            size: 28,
            color: 'white'
        }
    },

    paper_bgcolor: '#1e293b',

    font: {
        color: 'white'
    },

    scene: {

        xaxis: {
            title: 'Days'
        },

        yaxis: {
            title: 'Task Growth'
        },

        zaxis: {
            title: 'AI Accuracy'
        }
    },

    height: 700
},

{
    displayModeBar: false
});


// ===============================
// ANALYTICS PAGE GRAPH
// ===============================

Plotly.newPlot('analyticsLine',

[

{
    x: [1,2,3,4,5,6,7,8,9,10],

    y: [20,30,40,55,65,75,85,90,95,99],

    type: 'scatter',

    mode: 'lines+markers+text',

    text: [

        '20%',
        '30%',
        '40%',
        '55%',
        '65%',
        '75%',
        '85%',
        '90%',
        '95%',
        '99%'

    ],

    textposition: 'top center',

    line: {

        width: 6,

        color: '#22c55e'
    },

    marker: {

        size: 10,

        color: '#22c55e'
    }
}

],

{
    title: {

        text: '🔥 AI Productivity Analysis',

        font: {
            size: 28,
            color: 'white'
        }
    },

    paper_bgcolor: '#1e293b',

    plot_bgcolor: '#1e293b',

    font: {
        color: 'white'
    },

    xaxis: {
        title: 'Timeline'
    },

    yaxis: {
        title: 'Growth %'
    },

    height: 700
},

{
    displayModeBar: false
});


// ===============================
// TASK FUNCTIONS
// ===============================

function addTask() {

    let input =
        document.getElementById('taskInput');

    let value =
        input.value;

    if(value === '') {

        alert("Enter task");
        return;
    }

    let div =
        document.createElement('div');

    div.className = 'task';

    div.innerHTML = `

        <span>⏳ ${value}</span>

        <div>

            <button class="btn btn-success btn-sm"
                    onclick="completeTask(this)">

                Complete

            </button>

            <button class="btn btn-danger btn-sm"
                    onclick="deleteTask(this)">

                Delete

            </button>

        </div>
    `;

    document.getElementById('pendingTasks')
    .appendChild(div);

    input.value = '';

    updateCounts();

    showNotification('✅ Task Added Successfully');
}


// ===============================
// COMPLETE TASK
// ===============================

function completeTask(button) {

    let task =
        button.parentElement.parentElement;

    task.classList.add('completed');

    button.remove();

    document.getElementById('completedTasks')
    .appendChild(task);

    updateCounts();

    showNotification('🎉 Task Completed');
}


// ===============================
// DELETE TASK
// ===============================

function deleteTask(button) {

    button.parentElement.parentElement.remove();

    updateCounts();

    showNotification('❌ Task Deleted');
}


// ===============================
// UPDATE COUNTS
// ===============================

function updateCounts() {

    let pending =
        document.querySelectorAll(
            '#pendingTasks .task'
        ).length;

    let completed =
        document.querySelectorAll(
            '#completedTasks .task'
        ).length;

    let total =
        pending + completed;

    document.getElementById(
        'pendingCount'
    ).innerText = pending;

    document.getElementById(
        'completedCount'
    ).innerText = completed;

    document.getElementById(
        'totalTasks'
    ).innerText = total;

    updatePieChart(completed, pending);
}


// ===============================
// NOTIFICATIONS
// ===============================

function showNotification(message) {

    let box =
        document.getElementById('notification');

    box.innerText = message;

    box.style.display = 'block';

    setTimeout(() => {

        box.style.display = 'none';

    }, 3000);
}