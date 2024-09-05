import pytest
from nucleidechartlib.graphics.nucleide_sect import Nucleide_Sect
from nucleidechartlib.graphics.nucleide_table import Nucleide_Table
from nucleidechartlib.graphics.element_box import Element_Box
from utils import csv_driver

@pytest.fixture
def sample_elements():
    # Mock the elements data read from CSV
    return {
        '1H': {
            'nucleides': {
                'n1': {
                    'half_life': 'stable',
                    'decay_modes_intensities': 'N/A'
                }
            },
            'symbol': 'H',
            'mass_number': 1,
            'atomic_number': 1
        }
    }

def test_nucleide_sect(sample_elements):
    nucleide = Nucleide_Sect(id=1, name='H1', half_life='stable', decay_modes_intensities={}, extra={})
    assert nucleide.name == 'H1'
    assert nucleide.half_life == 'stable'
    assert nucleide.decay_modes_intensities == 'N/A'

def test_element_box(sample_elements):
    nucleide_boxes = {}
    for id, element in sample_elements.items():
        nucleide_boxes[id] = Nucleide_Sect(id=0, name=element['symbol'] + '1',
                                             half_life=element['nucleides']['n1']['half_life'],
                                             decay_modes_intensities=element['nucleides']['n1']['decay_modes_intensities'], extra={})

    element_box = Element_Box(id=1, name='Hydrogen', symbol='H', mass_number=1,
                               atomic_number=1, nucleides=nucleide_boxes)
    assert element_box.name == 'Hydrogen'
    assert element_box.symbol == 'H'
    assert len(element_box.nucleides) == 1

def test_nucleide_table(sample_elements):
    element_boxes = {}
    nucleide_boxes = {}
    for id, element in sample_elements.items():
        nucleide_boxes[id] = Nucleide_Sect(id=0, name=element['symbol'] + '1',
                                             half_life=element['nucleides']['n1']['half_life'],
                                             decay_modes_intensities=element['nucleides']['n1']['decay_modes_intensities'], extra={})
        element_boxes[id] = Element_Box(id=id, name=element['symbol'],
                                         symbol=element['symbol'],
                                         mass_number=element['mass_number'],
                                         atomic_number=element['atomic_number'],
                                         nucleides=nucleide_boxes)

    table = Nucleide_Table(id=0, name="Test Nucleide Table", element_boxes=element_boxes,
                           cols=18, rows=7)

    assert table.name == "Test Nucleide Table"
    assert len(table.element_boxes) == 1

def test_csv_read_elements(mocker):
    mock_csv_data = {
        '1H': {
            'nucleides': {
                'n1': {
                    'half_life': 'stable',
                    'decay_modes_intensities': 'N/A'
                }
            },
            'symbol': 'H',
            'mass_number': 1,
            'atomic_number': 1
        }
    }

    mocker.patch('..utils.csv_driver.read_elements', return_value=mock_csv_data)
    elements = csv_driver.read_elements('../datos.csv')
    assert len(elements) == 1
    assert elements['1H']['symbol'] == 'H'
